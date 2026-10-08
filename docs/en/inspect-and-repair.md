# Inspect and repair decision-history leakage

## Purpose

Use this guide when no effective-state boundary was established before writing, or when a draft already contains rejected ideas, old wording, internal reasons, or discussion residue. Identify material that responds only to an invisible drafting history, then restore a consistent document for its intended audience.

## Inspection prompt

Send this with the draft and available discussion records or modification plans:

```text
Inspect this draft for rejected ideas resurfacing and decision-history leakage. Do not edit it yet.

First reconstruct from discussion records, modification plans, and the latest explicit decisions:
1. Current effective content.
2. Superseded or rejected content.
3. Revision reasons used only for internal decisions.
4. Unresolved matters.

For each suspected instance, provide:
- Its location and original sentence.
- The older option, internal reason, or resolved issue it refers to.
- Whether the intended reader actually needs the information.
- A recommendation: retain, delete, rewrite directly, or clarify.
- Suggested wording without irrelevant decision history when a change is needed.

Wait for my confirmation of the findings before editing. Once the findings are resolved, extract a clean repair list and apply the changes together.

Do not mechanically treat every negative expression as an error. Retain genuine limitations, necessary exclusions, safety conditions, legal boundaries, and reader-relevant comparisons. Judge by the information's purpose, not by grammatical negativity.
```

This prompt chooses inspection before editing. Use it when that review mode fits the task.

## 1. Recover the effective state

If no decision record exists, reconstruct a provisional table:

| Content | Current status | Evidence | Eligible for draft? |
| --- | --- | --- | --- |
| Approach, definition, or wording | Approved / rejected / superseded / unresolved | Latest user decision or authoritative source | Yes / no / pending |

Later explicit decisions take precedence. Discussion does not imply approval. Keep unresolved matters open. Treat modification reasons as internal unless the reader needs them. Ask about a material ambiguity rather than guessing during cleanup.

## 2. Locate candidate passages

| Signal | Examples | What to check |
| --- | --- | --- |
| Version history | “no longer”, “previously”, “the old approach”, “now changed to” | Is this only describing a revision? |
| Denial of a rejected option | “not X but Y”, “does not use”, “does not require” | Could the excluded concept simply be absent? |
| Internal defense | “to avoid misunderstanding”, “it should be emphasized”, “although…however…” | Does this answer a discussion participant rather than the final reader? |
| Revision rationale | “because we previously”, “to address the review comment”, “therefore removed” | Does it belong in a change record? |
| Implicit residue | Old terms, variables, numbers, steps, or table structures | Does the current document still assume a discarded approach? |

Check headings, abstracts, examples, figures, and summaries as well as the body. A draft can preserve an obsolete concept without using a negative word, or keep answering a question that only arose under an old approach.

## 3. Classify each finding

```markdown
## Finding ID

- Location:
- Original text:
- Related historical material:
- Necessary for the intended reader: yes / no / unclear
- Recommendation: retain / delete / rewrite directly / clarify
- Suggested wording:
- Internal reason — exclude from draft:
- Status: awaiting discussion / resolved
```

## 4. Extract a clean repair list

After the findings have been resolved, extract only the final operations. Do not retell rejected options or their detailed reasons.

```markdown
# Clean repair list

## Delete
- Location:
  Deletion target:

## Replace
- Location:
  Final text:

## Add
- Location:
  Final text:

## Retain
- Location and content:

## Synchronize
- Corresponding locations in title, abstract, body, examples, tables, figures, and attachments:
```

## 5. Verify the repaired draft

- [ ] Deleted concepts have not returned inside denials.
- [ ] Internal revision reasons are absent from the final artifact.
- [ ] The draft makes sense without an invisible older version.
- [ ] Necessary limitations, exclusions, and risk explanations remain intact.
- [ ] Each repair follows a confirmed finding.
- [ ] Corresponding content is synchronized throughout the artifact and figures.
- [ ] A reader unfamiliar with the discussion can understand the document independently.

## Short prompt

```text
First inspect this draft for rejected ideas resurfacing or decision-history leakage without editing it. List candidate sentences, identify any rejected option, old version, or internal revision reason behind them, and assess whether the intended reader needs that information. Recommend retaining, deleting, rewriting directly, or clarifying each case. After I confirm the findings, extract a clean list of final operations and apply the repairs together.
```
