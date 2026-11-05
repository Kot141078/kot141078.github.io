# V78 five-image and ordered-gallery audit

Five actual owner Downloads regular JPEGs measured before ingest:nonzero,magic/format/decode/dimensions/visual inspection PASS. Source,destination and production bytes match exactly. No cropping,resizing,compression,EXIF rewrite,merge,reorder,discard,synthesis,fallback or extra thumbnail.

| ENTRY/position | Windows source | Repo destination | Bytes | Dimensions | Source SHA-256 | Destination SHA-256 |
| --- | --- | --- | --- | --- | --- | --- |
| 0273/1 | C:\Users\kotov\Downloads\1793298865195.jpg | assets/diary/the-chat-goes-quiet-the-compute-does-not/cover.jpg | 324085 | 1536×1024 | 03d4bb9c0b44f00803eb294e5d942793341c90972d917962ea4af220b313f1f5 | 03d4bb9c0b44f00803eb294e5d942793341c90972d917962ea4af220b313f1f5 |
| 0274/1 | C:\Users\kotov\Downloads\1793626616594.jpg | assets/diary/a-torn-flour-sack-is-a-harder-robotics-test-than-a-perfect-demo/cover.jpg | 296643 | 1672×941 | 03b1da51c25d7f4bb518db31598552f8c2a4127e425987dabc29e9537d47213c | 03b1da51c25d7f4bb518db31598552f8c2a4127e425987dabc29e9537d47213c |
| 0274/2 | C:\Users\kotov\Downloads\1793626616957.jpg | assets/diary/a-torn-flour-sack-is-a-harder-robotics-test-than-a-perfect-demo/image-02.jpg | 285939 | 1672×941 | d9c77847dc1462411534a8368d233cfb5f1756a06481be2c5da7adffd0f035be | d9c77847dc1462411534a8368d233cfb5f1756a06481be2c5da7adffd0f035be |
| 0275/1 | C:\Users\kotov\Downloads\1793653391660.jpg | assets/diary/sam-5-utilization-is-not-95-waste/cover.jpg | 239893 | 1672×941 | fe433b479418e84e242daf83c4b0557cd08c7a41baa390bae0f5ca8f06181e79 | fe433b479418e84e242daf83c4b0557cd08c7a41baa390bae0f5ca8f06181e79 |
| 0276/1 | C:\Users\kotov\Downloads\1793787542158.jpg | assets/diary/domino-drift-when-ai-argues-with-a-claim-you-never-made/cover.jpg | 259446 | 1122×1402 | e3bfe21258c50429cc4fd104addb1f23a70ad022ff59c945f32d04e31b0c997b | e3bfe21258c50429cc4fd104addb1f23a70ad022ff59c945f32d04e31b0c997b |

## ENTRY0274 owner order

1.1793626616594.jpg -> cover.jpg:flour-sack/spill scene.
2.1793626616957.jpg -> image-02.jpg:dough/scales scene.

Source primary_image is cover.jpg;extra_images contains exactly image-02.jpg. Existing gallery renderer displays primary first then image02;exactly two img nodes in that order at desktop/mobile,no blank shell. Existing list/archive/home convention only uses primary when images are shown. Other new posts have one cover each. Shared factual alt describes visible baker/robotic-arm/bakery workspace;existing renderer appends image2of2 to the second alt without new schema. No people/workplace/provenance/runtime facts inferred.

Legacy gallery0216 retains5 images;0233 retains3;0263 restored cover SHA-256 `dc7f230633d74e9ee9468f41457794c80941bfa407376f7c6a2fe48c5e8ccdb8`(1122×1402,308006 bytes) and source/correction audit preserved. Old post changes are related sections only. Local/production decode,old-gallery byte checks and protected-source hashes PASS.
