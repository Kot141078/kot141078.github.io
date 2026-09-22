# V72 Image Audit

All sources were detected as JPEG images and copied byte-for-byte as `cover.jpg` without a transformation pipeline.

| Entry | Source absolute path | Dimensions | Source bytes | SHA-256 | Destination | Destination bytes | Transformed |
| --- | --- | ---: | ---: | --- | --- | ---: | --- |
| 0241 | `C:\Users\kotov\Downloads\1789568086399.jpg` | 1280 x 720 | 216073 | `22d7f599015a97cea61a2d0431ce27b6fe8cc11ae04b49e64432881ba7f85e47` | `assets/diary/equality-and-sameness-are-not-the-same-thing/cover.jpg` | 216073 | no |
| 0242 | `C:\Users\kotov\Downloads\1789605773098.jpg` | 1280 x 720 | 135837 | `5c80a1f1053ba4274b1177acd3aefc2508bcefd8da008fceeac41fe346bab00f` | `assets/diary/every-complaining-gamer-is-basically-a-millionaire/cover.jpg` | 135837 | no |
| 0243 | `C:\Users\kotov\Downloads\1789641906488.jpg` | 1280 x 720 | 171119 | `20092e812e73a3acca05efc6f70351b2023fa5f7bd0a9cb75c812d6ff133dffd` | `assets/diary/provider-exit-must-be-a-boring-routine-otherwise-you-are-a-hostage/cover.jpg` | 171119 | no |
| 0244 | `C:\Users\kotov\Downloads\1789785793566.jpg` | 1280 x 698 | 124240 | `8a0fbb9694c6b071125241ea43f32f8751cf15fa1d09f102fd1e9f7aafae345a` | `assets/diary/the-abyss-is-not-a-safety-plan/cover.jpg` | 124240 | no |
| 0245 | `C:\Users\kotov\Downloads\1789842204577.jpg` | 1280 x 720 | 119933 | `12c89323e88bca51f681d6fcef1a55bd4444442fbc66f6651a1d87b0f9fe1942` | `assets/diary/the-next-ai-breakthrough-should-not-require-a-geek-to-assemble-it/cover.jpg` | 119933 | no |
| 0246 | `C:\Users\kotov\Downloads\1789947120643.jpg` | 1122 x 1402 | 165100 | `4c02fc7a0a5884944991ed2b74b07515a44d8d1590b10be9923a230616e256d4` | `assets/diary/what-body-should-an-ai-have/cover.jpg` | 165100 | no |
| 0247 | `C:\Users\kotov\Downloads\1790097610610.jpg` | 1122 x 1402 | 194228 | `0e866995777527f5315ef5d800e978109ab457362a1bcf6234bda77d5ea29ae1` | `assets/diary/the-human-in-the-loop-also-needs-a-budget/cover.jpg` | 194228 | no |

Destination format: JPEG for all seven. Destination SHA-256 equals the displayed source SHA-256 in every row. Expected/found/destination counts are 7/7/7; byte-identical count 7; transformed count 0. Local and remote rendering passed, and all seven deployed bytes match local SHA-256 values.
