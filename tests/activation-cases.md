# Manual activation and behavior cases

Status: documented acceptance cases; not executed as independent model evaluations. Package validation does not establish activation accuracy.

Run in an isolated conversation with the packaged skill available. Record host, model, date, actual selection, output, and pass/fail. Explicit calls test execution behavior; implicit requests test discovery as well. Judge semantic behavior rather than exact phrasing.

| Type | Request and supplied context | Expected behavior |
| --- | --- | --- |
| Direct | “Use $cleanroom-writing to draft our final policy.” Context: monthly approved, weekly rejected. | Draft monthly policy; omit rejected schedule and internal reasons. |
| Indirect | “We settled on the third introduction. Prepare the submission version from the approved claims.” Supply all three versions and the decision. | Appropriate implicit selection; draft approved claims only. |
| Indirect, Chinese | “按最后确认的修改统一修订摘要、正文和表格。” Supply approved monthly interval and outdated weekly references. | Appropriate implicit selection; consistent monthly wording throughout. |
| Output language | Chinese discussion; “交付英文定稿”; approved monthly reports. | English output with current approved schedule. |
| Source language | English document plus Chinese request to apply approved revisions, with no output-language instruction. | Preserve English document language. |
| Boundary | Final policy requested while monthly versus quarterly remains unresolved. | Clarify material decision; do not silently select. |
| Boundary | “Inspect for leakage; do not edit until I confirm.” | Findings only; preserve the user's review stage. |
| Necessary negative | Approved rule: source documents must not be uploaded. | Keep the prohibition in the artifact. |
| Necessary comparison | Final buyer guide must compare two approved products. | Keep reader-relevant comparison. |
| Negative | “Brainstorm three alternative manuscript structures.” | Do not impose final-draft filtering or use this skill for brainstorming. |
| Negative | “Write a decision log explaining why A was rejected.” | Preserve decision history; do not use this skill to remove it. |
| Negative | “Draft a reviewer response explaining our revisions.” | Preserve requested revision rationale. |
| Negative | “Plot the scientific figure from this CSV.” | Do not select solely for plotting. |
| Negative | “Compile this LaTeX file.” | Do not select solely for compilation. |
| Negative | “Convert CSV to JSON.” | Do not select solely for conversion. |
| Negative | “Run the quick unit test.” | Do not select solely for test execution. |

For final artifacts, also check that excluded-history ledgers and the workflow itself are absent unless requested. The relevant document-format workflow may still be needed for actual file edits.
