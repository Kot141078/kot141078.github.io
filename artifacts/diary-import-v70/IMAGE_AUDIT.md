# V70 Image Audit

Seven supplied JPEGs were admitted. Each normalized repository asset is byte-identical to its supplied source file and to the deployed HTTP response.

| Entry | Supplied file | Repository asset | Bytes | Dimensions | SHA-256 |
| --- | --- | --- | ---: | --- | --- |
| 0231 | `1788331573681.jpg` | `assets/diary/the-agent-is-entering-the-payment-rail/cover.jpg` | 133753 | 1280x720 | `ba3a1ceba7835fb8a7d94de886e761555621a4ef2ef30902a856640cd1068675` |
| 0232 | `1788505302332.jpg` | `assets/diary/meta-has-just-published-something-more-important-than-another-model-benchmark-an-ai-architecture-in-which-the-durable-part-of-the-system-lives-outside-the-model/cover.jpg` | 139067 | 1280x720 | `17d5d746570be7fc2387ad44549f4089856edea6ce3239049af89837bb7f5efd` |
| 0233 | `1788718291045.jpg` | `assets/diary/i-do-not-just-want-ai-in-a-game/cover.jpg` | 189884 | 1280x720 | `7261dfad74de574bcff2ebedac93950702894b1258b14b5a29c49d61d5ee72ea` |
| 0233 | `1788718290877.jpg` | `assets/diary/i-do-not-just-want-ai-in-a-game/image-02.jpg` | 243772 | 1280x720 | `6b7a60a0eab9c3b56d71e4c4798bf526ef9d6cea33798cadb48ea07058944a5e` |
| 0233 | `1788718290995.jpg` | `assets/diary/i-do-not-just-want-ai-in-a-game/image-03.jpg` | 218705 | 1280x720 | `d2587f794eb5042a7216ca46055237bef8f716ed86436c383b54cfd84dfe468e` |
| 0234 | `1788772389396.jpg` | `assets/diary/ai-is-not-only-a-productivity-multiplier-it-is-a-strategy-multiplier/cover.jpg` | 208235 | 1280x720 | `182e3a9ca9a7b413d46ece92ae7f5f4078c5fb9d1f35fc34d507a4d0c48b8bf0` |
| 0235 | `1788853457613.jpg` | `assets/diary/ai-scale-needs-three-licenses/cover.jpg` | 184563 | 1280x720 | `32241c656be6fe4169f4600810c05a3504a7dd6bcd30fbf2ffce978a88c3849a` |

## Gallery order

ENTRY 0233 exact order:

1. `cover.jpg` from `1788718291045.jpg`
2. `image-02.jpg` from `1788718290877.jpg`
3. `image-03.jpg` from `1788718290995.jpg`

The first image is the article lead and card cover; the latter two are ordered gallery items. Desktop uses two gallery columns, mobile uses one, with zero horizontal overflow.

## Validation result

- Local decode: 7/7.
- Remote HTTP 200 and `image/jpeg`: 7/7.
- Remote/local/supplied byte equality: 7/7.
- Placeholder or blank image: 0.
- Missing local reference: 0.
- Broken loaded image in local/remote browser checks: 0.
- ENTRY 0216 gallery regression: pass, five images intact.
