# Vision V64 Before After Visual Check

Verdict: PASS.

Screenshot directory:

`C:\Users\kotov\Downloads\111\vision-v64-visual\`

Before/package receipts:

- `before-home-desktop-1440x900.png`
- `before-start-here-desktop-1440x900.png`
- `before-agi-desktop-1440x900.png`
- `package-preview-desktop-1440x900.png`
- `package-preview-mobile-390x844.png`

Local after receipts:

- `after-local-vision-desktop-1920.png` 1920x1080 SHA-256 `ef869e5bc7abe1986c31ca44a5da4767ebcd94808979d68b619a35f793e06e45`
- `after-local-vision-desktop-1440x900.png` 1440x900 SHA-256 `dbf83691686fb0c33e2fbcdb9127e1ae233d5657f9dc1bb60a613ac3338cfada`
- `after-local-vision-tablet-768x900.png` 768x900 SHA-256 `bc5bd5d691be955db9989ee3dbce30fc8109ae0797bc3b1b2188b0a5b91a4bfb`
- `after-local-vision-mobile-390x844.png` 390x844 SHA-256 `7ff3c45697fd6821ed474171a69321db9a3702be2721354edea50ba71647f11d`
- `after-local-vision-mobile-360x800.png` 360x800 SHA-256 `a87028cc7eb32a5dfff0b7e7399600db130bdc582cba32e045fe405391676b67`
- `after-local-vision-narrow-320x700.png` 320x700 SHA-256 `c8a37825f457ee6b5122ec1ce7161fab584af762c0d2c30aad9e7e0214e24749`
- `after-local-vision-full-page.png` 1425x12947 SHA-256 `dc2e49923b9dd7c23843c7792c48c2b57e271a79bd989cabe84b7574ab3c58e9`
- `after-local-vision-print-a4.pdf` SHA-256 `4059c4c9b640030f6d6f335cd1ffdaeeb801eeec5ef423c4340f7c0f24cf4e99`
- `after-local-home-vision-card.png` SHA-256 `18f29fae34d515bde45475c318b0e337d5768aa08d2ac44c0f3916ed2c39bc6e`
- `after-local-start-here-vision-callout.png` SHA-256 `dbe5026e88c57e6ab9e6d6883ba2c71fdd9b2f845a9c82fe2a7bf2650cfb6860`
- `after-local-agi-vision-card.png` SHA-256 `8c85ee656c3b7636e19c026a902bfe162a57fcd509d742ebf6af36a62f83be7e`

Remote final receipts:

- `final-remote-vision-desktop-1440x900.png` 1440x900 SHA-256 `dbf83691686fb0c33e2fbcdb9127e1ae233d5657f9dc1bb60a613ac3338cfada`
- `final-remote-vision-mobile-390x844.png` 390x844 SHA-256 `5bc9df558cc6b34785ceffb3562b3f8e09e009779d063aa2ab8b399ca7571137`
- `final-remote-vision-full-page.png` 1425x12947 SHA-256 `dc2e49923b9dd7c23843c7792c48c2b57e271a79bd989cabe84b7574ab3c58e9`
- `final-remote-vision-print-a4.pdf` SHA-256 `7b56ad85695aeb5fde963315aa33ab5634eb8ab0b2d7e2864ac82a11df682c37`
- `final-remote-home-vision-card.png` SHA-256 `18f29fae34d515bde45475c318b0e337d5768aa08d2ac44c0f3916ed2c39bc6e`
- `final-remote-start-here-vision-callout.png` SHA-256 `dbe5026e88c57e6ab9e6d6883ba2c71fdd9b2f845a9c82fe2a7bf2650cfb6860`

Visual checks:

- PNG receipts nonblank: PASS.
- PDF receipts have `%PDF-` header: PASS.
- Desktop nav wraps cleanly: PASS.
- Mobile nav remains visible and keyboard-addressable: PASS.
- CDP overflow metrics: `scrollWidth == clientWidth` for 1920, 1440, 768, 390, 360, and 320 widths.
- Print rendering generated: PASS.

