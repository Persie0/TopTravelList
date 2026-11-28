# Worldwide audit consolidation — pass 221, part 2

2026-11-27. Original blobs from PRs #351–359 consolidated into #384 without changing score values. All source branches remain open. Accepted score patches change only null core fields into numeric values. New standalone reviews copied unchanged; their factual assertions and numerical calibration are not independently verified here.

| Source PR | Changed files | New score files | New review notes |
|---|---:|---:|---:|
| 359 | 22 | 16 | 2 |
| 358 | 22 | 2 | 2 |
| 357 | 22 | 20 | 2 |
| 356 | 22 | 15 | 2 |
| 355 | 22 | 12 | 2 |
| 354 | 23 | 20 | 2 |
| 353 | 4 | 2 | 1 |
| 352 | 5 | 4 | 1 |
| 351 | 3 | 2 | 1 |

93 additional unique score files and 15 review notes, plus 180 scores and 26 reviews in part 1. One identical duplicate skipped. Eighteen conflicting alternatives retained on their source branches, existing consolidated versions kept provisionally. No claim that existing ratings are superior.

| Alternative PR | Path | Selected PR | Selected blob | Alternative blob |
|---|---|---|---|---|
| 358 | countries/AE/sights/abu-dhabi-sabkha.yaml | #384 | 0c5e9a7c36a8671673eb2be82d5e7445931d3fcc | afabe6b8d9ac982bed34288f72e764c08cfe2f54 |
| 358 | countries/AE/sights/ed-dur-archaeological-site.yaml | #384 | 962c0164bd55c64102c35a0a689b75b2dab04312 | aead84a1454b2e70e6648b7cc55aa82e71f527c0 |
| 358 | countries/AE/sights/julfar-trading-town-archaeological-landscape.yaml | #384 | 41bcf61088e63e20c2ba4178ccaa52fd43488825 | 14d945834f7732ed312682ec8445f41bd9cc666a |
| 358 | countries/AE/sights/sir-bu-nair-island.yaml | #384 | 1bc2a02124dd2f4d6fbe665dbc91afcf0fb5e8b7 | d0dd2937cae9ca958809494426f3e7f0cba278b6 |
| 358 | countries/AE/sights/umm-an-nar-settlement-and-cemetery.yaml | #384 | 31dc8bc4b9b2ed2c62633db06c9be9c260b75180 | 7ab481041b93544bf95be5929f8d18ec85d753d0 |
| 358 | countries/AG/sights/redonda-ecosystem-reserve.yaml | #384 | 1700c95b973c6587537851127dbb3090ba1d6d47 | a1de101147b38cc1803e08343e76ceed7169d6e5 |
| 358 | countries/AI/sights/fountain-cavern.yaml | #384 | 1832ab5427a6ee784c1b4f39c9b52375de72b944 | d7d03a27e06bfa51dfa07f5847dab5b5e324af0c |
| 358 | countries/AZ/sights/azykh-and-taghlar-prehistoric-caves.yaml | #384 | a61ea5828f22bab428b2f36f9ddd9a57607f7110 | 1c5e792e292315d96dde4a25f0f7cad8206d2646 |
| 358 | countries/AZ/sights/baku-stage-mountain.yaml | #384 | 0544cab4cf212dd5f0d9f6e27c79fceb46c8767c | dbfa2c6f9a91444ea17eb076abfd9519dcd7a62a |
| 358 | countries/AZ/sights/binegadi-quaternary-fauna-and-flora-deposit.yaml | #384 | 38d94365958b65ac7282227e27f552db14de0e95 | 904c71682b4ea28d67b68074bfa2d31c4976be1e |
| 358 | countries/AZ/sights/khudafarin-bridges-and-related-sites.yaml | #384 | f0ba7c022e5168e82c6129fab82077ca91dd91a0 | c1c241180a874395065c5e73e729b3a7fad9ced2 |
| 358 | countries/AZ/sights/lokbatan-mud-cone.yaml | #384 | 59e8c671c91ad046f42c8861b956600ab263edb0 | 07749b505d65bba1fddc1bac78d6d2a40329a126 |
| 358 | countries/BJ/sights/pendjari-national-park.yaml | #384 | b1cc8ff927f457b5b71d3f02fef294f0f4bd2407 | 9b8b541840d4cfb4ea71f9ca98c042129e0a680a |
| 358 | countries/BT/sights/jomotsangkha-wildlife-sanctuary.yaml | #384 | 59d54c782c7db34b3d5b15b5665107459fd4a071 | 790803786a06e32314551902074d34fc705cbfc4 |
| 358 | countries/BT/sights/phibsoo-wildlife-sanctuary.yaml | #384 | 318573674f9f9dec9c429ca18cbc7ef31eb577d1 | 5e237ecbed9072814d493c7231344c16e6e44c53 |
| 358 | countries/BZ/sights/burdon-canal-nature-reserve.yaml | #384 | 669c21423806ad4864ed05f39f3af6e53d238e89 | 37c25360edcb443a3011a3b6a61172af403211f0 |
| 358 | countries/BZ/sights/chiquibul-national-park.yaml | #384 | ec47c9c61fc5f7a24465627f62d3ff8d4557ee18 | b0eb40109790b6d3f54501f3699f5623f247bf86 |
| 353 | countries/KI/sights/phoenix-islands-protected-area.yaml | #384 | b6105640f3e52823f570ed1b9c6d7efb8f65d3d8 | bc4de3787d173d2945f917eb626364cddc82c8cd |

## Excluded changes requiring individual reconciliation

| Source PR | Path | Reason | Blob |
|---|---|---|---|
| 359 | countries/CU/sights/aqueduct-of-albear.yaml | not null-only | 3a9be27226823158f2c7b822ac54f0a766eb9440 |
| 359 | countries/CU/sights/first-coffee-plantations-landscape.yaml | not null-only | e0024c5ce26c6adb9c63ced0d31421854dc31323 |
| 359 | countries/GT/sights/naj-tunich-cave.yaml | not null-only | ecf187fe2083d5ae618ef25e810c697aa0e45b81 |
| 359 | countries/GT/sights/san-bartolo-murals.yaml | not null-only | f989fe6c15ec718702fae9add7953ffacd5f607c |
| 356 | countries/CD/sights/lomami-national-park.yaml | not null-only | ba355561836df6d01fd7541e39250a1e052b40f6 |
| 356 | countries/CD/sights/okapi-wildlife-reserve.yaml | not null-only | f69aec510ca046ad7324b8824a61b0464cdb989e |
| 356 | countries/CD/sights/salonga-national-park.yaml | not null-only | 7cbe81609a08c159c931f3e2ec6c9781c1e6c501 |
| 356 | countries/CG/sights/tchimpounga-chimpanzee-sanctuary.yaml | not null-only | d12626e631be4b0df8b06a18a59b7f98ceef0dcd |
| 356 | countries/GN/sights/mount-nimba-strict-nature-reserve-guinea-sector.yaml | not null-only | 14044adeec7c29f74d9f6b66f09ebd3530f63553 |
| 355 | countries/CX/sights/winifred-beach.yaml | not null-only | 4a6bbe5469bd67b7527ae61c8e38290e3c617007 |
| 355 | countries/ET/sights/dirre-sheikh-hussein.yaml | not null-only | 089f27d0b09d24772bd4fe9bacc510dc3c7c9800 |
| 355 | countries/ET/sights/negash-village.yaml | not null-only | 6410a19b7e222d4f4d9aba9dd9b5e4fbce6f2ab3 |
| 355 | countries/ET/sights/sacred-landscapes-tigray.yaml | not null-only | 9dcd20a0c06a5129578314e5ce1245d7191f8e73 |
| 355 | countries/JO/sights/fifa-nature-reserve.yaml | not null-only | 10bdb94c26e436807fdef52b65df567f65dd5fba |
| 355 | countries/KW/sights/kuwait-zoo.yaml | not null-only | 6ccacf756dc2e84f274e0501d46b0d79745be953 |
| 355 | countries/LA/sights/phou-bia.yaml | not null-only | 20d841885b51f317a64d4b5eb4b7f7ae94e8257c |
| 355 | countries/MA/sights/el-gour.yaml | not null-only | afffdd63e68f9744a81981390f1c599394043fd3 |
| 354 | methodology/evidence-and-quality-standard.md | non-score/non-additive review | 7fa31d8b2f05a2c6050e78044e9abe2a389719f8 |

Seventeen YAML files with edits beyond null-only core fills and one evidence-standard change were not imported. These must be reviewed, not discarded. Source review notes do not mean the associated excluded scores were accepted. Earlier pass 220 documented 20 conflicting alternatives; cumulative 38 alternative conflicts recorded. No newly assessed worldwide records; 1570/1590 remains the previous cross-branch coverage estimate, with 20 incomplete, not yet a validated consolidated count. Full validation, evidence verification, review links, conflict reconciliation, ranking generation and merge pending. No manually dispatched Actions.
