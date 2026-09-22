# V71 Image Audit

Four source images were supplied and four destination assets were created. The established flow was byte-preserving; transformed count is zero. ENTRY 0239 is intentionally image-less.

| Entry | Source absolute path | Format | Dimensions | Source bytes | SHA-256 | Destination | Destination format | Destination bytes | Destination SHA-256 | Transformed |
| --- | --- | --- | --- | ---: | --- | --- | --- | ---: | --- | --- |
| 0236 | `C:\Users\kotov\Downloads\1788888434035.jpg` | JPEG | 1280 x 720 | 150866 | `1d24e5b9d39d89cfd5c2aadf90be5681f4cb7840d76f3888edd3f7f120cd25c2` | `assets/diary/the-ai-did-not-rebel/cover.jpg` | JPEG | 150866 | `1d24e5b9d39d89cfd5c2aadf90be5681f4cb7840d76f3888edd3f7f120cd25c2` | no |
| 0237 | `C:\Users\kotov\Downloads\1788973235299.jpg` | JPEG | 1280 x 720 | 198945 | `df5c368dfced36c40ec718261d7ab80d4cd7d398a6d99815e510b5536ff68cca` | `assets/diary/the-benchmark-score-did-not-belong-to-the-model/cover.jpg` | JPEG | 198945 | `df5c368dfced36c40ec718261d7ab80d4cd7d398a6d99815e510b5536ff68cca` | no |
| 0238 | `C:\Users\kotov\Downloads\1789135797307.jpg` | JPEG | 1280 x 720 | 148519 | `32147ece3c4a215d61a359300ccbdd8f774bbade955d6c4294dba3ca939465de` | `assets/diary/ai-as-a-camera-of-thought/cover.jpg` | JPEG | 148519 | `32147ece3c4a215d61a359300ccbdd8f774bbade955d6c4294dba3ca939465de` | no |
| 0240 | `C:\Users\kotov\Downloads\1789473971115.jpg` | JPEG | 1280 x 720 | 187395 | `2de0ebb040077d88e7f5e3b8323361e449ce91111e2ff974bd0e5b0be23d96b7` | `assets/diary/an-octopus-at-every-workstation-a-digital-mycelium-between-them/cover.jpg` | JPEG | 187395 | `2de0ebb040077d88e7f5e3b8323361e449ce91111e2ff974bd0e5b0be23d96b7` | no |

All source files were non-zero, valid by image decoder, and visually inspected. All four deployed assets return HTTP 200 and match local SHA-256 exactly. No placeholder, borrowed image, generated fallback, or new processing pipeline was used.

ENTRY 0239 has empty `primary_image`, `image_alt`, and `extra_images` source fields; its machine object omits image fields and its rendered page contains zero `<img>` elements.
