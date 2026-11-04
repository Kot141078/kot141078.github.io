# V73 existing candidate integrity manifest

All ten files existed before recovery. Full Windows paths, byte counts and measured SHA-256 were captured after read-only Phase A admission and before attribute changes. Pre/post hashes remain identical after repair, two builds, the full machine gate and production verification. These are recovery hashes, not a re-hash of the original uploaded text attachment.

| Absolute path | Bytes | Before SHA-256 | After SHA-256 | Result |
| --- | --- | --- | --- | --- |
| C:\Users\kotov\Desktop\AGI\kot141078.github.io\assets\diary\i-bought-a-5-000-graphics-card\cover.jpg | 257559 | 51575785e25a1b43c0a2d68020181e123856e6b8f2376656765e3d23d54e9334 | 51575785e25a1b43c0a2d68020181e123856e6b8f2376656765e3d23d54e9334 | IDENTICAL |
| C:\Users\kotov\Desktop\AGI\kot141078.github.io\assets\diary\i-have-often-argued-that-personal-ai-memory-should-remain-local\cover.jpg | 222430 | eb14c551bc9f47efc14a3bc28d7d78f10473940c2b62d4630db4ec6765a3c8b8 | eb14c551bc9f47efc14a3bc28d7d78f10473940c2b62d4630db4ec6765a3c8b8 | IDENTICAL |
| C:\Users\kotov\Desktop\AGI\kot141078.github.io\assets\diary\maybe-uncle-jensen-huang-simply-forgot-to-mention-that-he-was-using-my-terminology\cover.jpg | 181814 | 2425ff625e7fbc8058c5dc7fb1f1def33c7ee9a5b6fde35206d6b42643d34584 | 2425ff625e7fbc8058c5dc7fb1f1def33c7ee9a5b6fde35206d6b42643d34584 | IDENTICAL |
| C:\Users\kotov\Desktop\AGI\kot141078.github.io\assets\diary\speaking-the-same-language-does-not-mean-seeing-the-same-world\cover.jpg | 280117 | d2dfbe6abd8b666e42957e8fa0a1359e81f52443ca4b4fa701318294128906b5 | d2dfbe6abd8b666e42957e8fa0a1359e81f52443ca4b4fa701318294128906b5 | IDENTICAL |
| C:\Users\kotov\Desktop\AGI\kot141078.github.io\assets\diary\when-ai-multiplies-hypotheses-scientific-taste-becomes-a-practical-problem\cover.jpg | 252117 | a2eb9d110ce8244291e5f05a3853e9d6ca0551f5672db2be25602b8ec1287ffc | a2eb9d110ce8244291e5f05a3853e9d6ca0551f5672db2be25602b8ec1287ffc | IDENTICAL |
| C:\Users\kotov\Desktop\AGI\kot141078.github.io\content\diary\i-bought-a-5-000-graphics-card.md | 2909 | c5fab1368804c62474af3c344a15d3d8363ec86981c58373f7a7cd07b89e855b | c5fab1368804c62474af3c344a15d3d8363ec86981c58373f7a7cd07b89e855b | IDENTICAL |
| C:\Users\kotov\Desktop\AGI\kot141078.github.io\content\diary\i-have-often-argued-that-personal-ai-memory-should-remain-local.md | 3414 | bfa7decc633f02ef4192c377e65b00fb57516faf7e9d8ee9309a589572154de5 | bfa7decc633f02ef4192c377e65b00fb57516faf7e9d8ee9309a589572154de5 | IDENTICAL |
| C:\Users\kotov\Desktop\AGI\kot141078.github.io\content\diary\maybe-uncle-jensen-huang-simply-forgot-to-mention-that-he-was-using-my-terminology.md | 2908 | f98488c7285141bc135891a3c7304abda63d748792d0cb3e6f19e63a2acb6e70 | f98488c7285141bc135891a3c7304abda63d748792d0cb3e6f19e63a2acb6e70 | IDENTICAL |
| C:\Users\kotov\Desktop\AGI\kot141078.github.io\content\diary\speaking-the-same-language-does-not-mean-seeing-the-same-world.md | 3320 | 49d6bd90cbc8541f00bf87de35d1c21cef1f1d1a6d3bdd118180a7956e6093c9 | 49d6bd90cbc8541f00bf87de35d1c21cef1f1d1a6d3bdd118180a7956e6093c9 | IDENTICAL |
| C:\Users\kotov\Desktop\AGI\kot141078.github.io\content\diary\when-ai-multiplies-hypotheses-scientific-taste-becomes-a-practical-problem.md | 3520 | 63824d6e1b883d320e50c900340273a168bf96e200b512be5fa149e837f3b230 | 63824d6e1b883d320e50c900340273a168bf96e200b512be5fa149e837f3b230 | IDENTICAL |

## Exact initial partial Git state

```text
 D diary/a-goal-can-be-installed/index.html
 M sitemap.xml
?? assets/diary/i-bought-a-5-000-graphics-card/cover.jpg
?? assets/diary/i-have-often-argued-that-personal-ai-memory-should-remain-local/cover.jpg
?? assets/diary/maybe-uncle-jensen-huang-simply-forgot-to-mention-that-he-was-using-my-terminology/cover.jpg
?? assets/diary/speaking-the-same-language-does-not-mean-seeing-the-same-world/cover.jpg
?? assets/diary/when-ai-multiplies-hypotheses-scientific-taste-becomes-a-practical-problem/cover.jpg
?? content/diary/i-bought-a-5-000-graphics-card.md
?? content/diary/i-have-often-argued-that-personal-ai-memory-should-remain-local.md
?? content/diary/maybe-uncle-jensen-huang-simply-forgot-to-mention-that-he-was-using-my-terminology.md
?? content/diary/speaking-the-same-language-does-not-mean-seeing-the-same-world.md
?? content/diary/when-ai-multiplies-hypotheses-scientific-taste-becomes-a-practical-problem.md
```

0 staged, 2 unstaged, 10 untracked. No untracked/ignored generated files or active Git operation. Local/remote HEAD matched the prepared baseline. No fetch/pull/reset/restore/clean/stash/manual deletion was used during dirty-candidate recovery.
