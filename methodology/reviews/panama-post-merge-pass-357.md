# Panama post-merge reconciliation — pass 357

Audit input: 24f6fbea66457f247ce59b64acddb49b9da799e7. Merge base with main: 3dc4631c5e17acf7fe75f1ab5334845017d232d7.

- 225 Panama sight YAML files in audit directory, 53 on main.
- All 53 original Git blob hashes identical; zero missing or modified originals.
- All 225 YAML filenames appear exactly once in ranked Markdown, with no dangling references.
- All 225 displayed weighted scores, score ranges, descending order and competition ranks checked in JavaScript; 26 scores >=90.
- Before this report, audit is 24 commits ahead and 3 behind main; 198 changed paths (172 new sight files, 24 audit reviews, two generated Markdown files). Main-side changes affect 11 web files only; the two changed-path sets do not overlap.
- GitHub commit search for pass 332 returned an unrelated Cambodia commit, so the historical pass remains unreconciled. No assertion of exhaustive tourism coverage.

No attraction scores changed in this pass. Full Python schema and generator verification remains necessary, as the above checks validate directory metadata and displayed rankings rather than parsing every YAML. If CI is needed, use the public Playground repository; no workflow dispatched in this pass. No merge performed.
