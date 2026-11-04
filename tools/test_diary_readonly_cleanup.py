"""Bounded fixtures for the Windows generated-Diary ReadOnly callback."""
import contextlib
import io
import os
from pathlib import Path
import stat
import tempfile
import unittest
from unittest.mock import patch

import build_diary as builder


@unittest.skipUnless(os.name == "nt", "Windows attribute behavior")
class GeneratedDiaryCleanupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="diary-readonly-test-")
        self.root = Path(self.temp.name).resolve() / "repo"
        self.diary = self.root / "diary"
        self.diary.mkdir(parents=True)
        self.sentinel = self.root / "source-sentinel.txt"
        self.sentinel.write_bytes(b"outside generated tree: unchanged")
        self.root_patch = patch.object(builder, "ROOT", self.root)
        self.diary_patch = patch.object(builder, "DIARY_DIR", self.diary)
        self.root_patch.start()
        self.diary_patch.start()

    def tearDown(self):
        self.diary_patch.stop()
        self.root_patch.stop()
        self.temp.cleanup()

    def error(self):
        error = PermissionError(13, "simulated Windows delete denial")
        error.winerror = 5
        return error

    def test_nested_readonly_file_and_directory(self):
        nested = self.diary / "nested"
        nested.mkdir()
        target = nested / "generated.html"
        target.write_bytes(b"fixture")
        os.chmod(target, stat.S_IREAD)
        os.chmod(nested, stat.S_IREAD)
        before = self.sentinel.read_bytes(), self.sentinel.stat().st_file_attributes
        log = io.StringIO()
        with contextlib.redirect_stdout(log):
            builder.wipe_generated_diary_tree()
        self.assertTrue(self.diary.is_dir())
        self.assertEqual(list(self.diary.iterdir()), [])
        self.assertIn(str(target), log.getvalue())
        self.assertIn(str(nested), log.getvalue())
        self.assertEqual(before, (self.sentinel.read_bytes(), self.sentinel.stat().st_file_attributes))
        print(log.getvalue(), end="")

    def test_normal_cleanup_and_second_empty_wipe(self):
        (self.diary / "generated.html").write_bytes(b"fixture")
        builder.wipe_generated_diary_tree()
        builder.wipe_generated_diary_tree()
        self.assertEqual(list(self.diary.iterdir()), [])

    def test_non_readonly_permission_error_propagates(self):
        target = self.diary / "generated.html"
        target.write_bytes(b"fixture")
        error = self.error()
        with patch.object(builder.os, "chmod") as change:
            with self.assertRaises(PermissionError) as caught:
                builder.retry_generated_readonly_delete(os.unlink, str(target), (type(error), error, None))
            self.assertIs(caught.exception, error)
            change.assert_not_called()
        self.assertEqual(target.read_bytes(), b"fixture")

    def test_outside_readonly_sentinel_rejected_unchanged(self):
        os.chmod(self.sentinel, stat.S_IREAD)
        before = self.sentinel.read_bytes(), self.sentinel.stat().st_file_attributes
        error = self.error()
        try:
            with self.assertRaises(PermissionError):
                builder.retry_generated_readonly_delete(os.unlink, str(self.sentinel), (type(error), error, None))
            self.assertEqual(before, (self.sentinel.read_bytes(), self.sentinel.stat().st_file_attributes))
        finally:
            os.chmod(self.sentinel, stat.S_IWRITE)

    def test_repeated_failure_retried_once_and_propagates(self):
        target = self.diary / "generated.html"
        target.write_bytes(b"fixture")
        os.chmod(target, stat.S_IREAD)
        before = target.stat().st_file_attributes
        error = self.error()
        with patch.object(builder.os, "unlink", side_effect=error) as remove:
            with self.assertRaises(PermissionError) as caught:
                builder.retry_generated_readonly_delete(remove, str(target), (type(error), error, None))
            self.assertIs(caught.exception, error)
            remove.assert_called_once_with(str(target))
        self.assertEqual(target.stat().st_file_attributes, before & ~stat.FILE_ATTRIBUTE_READONLY)
        self.assertEqual(target.read_bytes(), b"fixture")

    def test_reparse_item_rejected_before_chmod(self):
        target = self.diary / "generated.html"
        target.write_bytes(b"fixture")
        error = self.error()
        original = Path.lstat

        def reparse_info(path):
            if path == target:
                class Reparse:
                    st_file_attributes = stat.FILE_ATTRIBUTE_REPARSE_POINT | stat.FILE_ATTRIBUTE_READONLY
                return Reparse()
            return original(path)

        with patch.object(Path, "lstat", reparse_info), patch.object(builder.os, "chmod") as change:
            with self.assertRaises(PermissionError):
                builder.retry_generated_readonly_delete(os.unlink, str(target), (type(error), error, None))
            change.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
