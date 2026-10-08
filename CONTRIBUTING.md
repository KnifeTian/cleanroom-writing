# Contributing

Useful contributions include reproducible leakage examples, false-trigger reports, translation improvements, and narrow fixes supported by observed behavior.

For a report, include a synthetic conversation, the final requested deliverable, expected behavior, actual output, and host/model details. Remove personal information, confidential drafts, and credentials. Explain whether the issue concerns selection or execution after selection.

Keep English and Chinese guides aligned. Maintain one executable skill under `skills/cleanroom-writing`; put translated explanations in `docs/`. Preserve the distinction between unnecessary decision history and necessary comparisons or limitations.

Run `python scripts/validate_package.py`. Use the manual cases in `tests/activation-cases.md` when changing discovery or workflow behavior, and record what was actually evaluated.

This project is maintained by KnifeTian and licensed under the MIT License. Submit contributions that you have the right to share under that license.
