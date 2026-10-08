# Cleanroom Writing: background and applications

## The recurring problem

LLM-assisted writing often involves several alternatives, rejected approaches, revised definitions, and repeated edits. These conversations help establish the final decision, but discarded material can resurface in the deliverable.

Suppose a team compares approach A with approach B and approves B. A reader may only need a direct description of B. Yet the draft may say “This uses B rather than A” or “To avoid the earlier problem, this approach…”. The text carries an internal discussion into a document whose audience has never seen it.

We call this **rejected ideas resurfacing in the final draft**, or **decision-history leakage**. It can affect papers, patents, technical reports, policies, proposals, contract explanations, product copy, and ordinary business writing.

Rejected content remains available in the conversation. Repeated discussion may keep it salient, and explanatory or comparative prose can reintroduce it. This is the practical motivation for the workflow, rather than a measured claim about model internals.

## Purpose

Cleanroom Writing establishes an explicit content boundary between discussion and delivery. Exploration can preserve alternatives, failed ideas, and reasons for a decision. Appearing in the discussion does not by itself authorize content for the final draft.

The workflow aims to:

1. Separate confirmed content from discussion history.
2. Let later explicit decisions supersede earlier decisions.
3. Prevent rejected ideas from returning through denials, comparisons, disclaimers, or explanatory asides.
4. Keep internal revision reasons out of audience-facing prose when they do not serve the reader.
5. Align the body, abstract, examples, tables, figures, and attachments with the same final state.
6. Produce a document that makes sense independently of its drafting conversation.

## How it works

Recover an authoritative state before drafting:

| Category | Meaning | Treatment |
| --- | --- | --- |
| Approved content | Effective facts, claims, definitions, wording, and structure | Eligible for the draft |
| Approved changes | Confirmed edits | Apply to the draft |
| Excluded history | Rejected options, superseded decisions, old wording, internal reasons | Audit material only |
| Unresolved matters | Questions that still affect the outcome | Keep open; clarify when necessary |

Extract a clean brief or execution list containing only effective content and changes. Draft from that brief, then audit the artifact separately:

- Trace substantive statements to approved content or authoritative sources.
- Check definitions, numbers, choices, and wording against later decisions.
- Inspect whether excluded concepts return through “no longer”, “not X but Y”, or similar language.
- Remove internal selection reasons and references to invisible earlier drafts when the reader does not need them.
- Check the title, abstract, body, examples, tables, and figures for consistency.

Negative and comparative expressions are signals for review, not banned words. Preserve actual scope boundaries, necessary limitations, safety conditions, legal qualifications, and requested comparisons. The question is whether the information serves the intended reader.

## Applications and boundaries

Useful applications include final drafting after many discussions; applying an approved modification plan throughout a document; consolidating author comments, reviewer feedback, annotations, and older drafts; and cleaning residual terminology from repeated revisions. Formal documents such as patent drafts, papers, technical reports, policies, project applications, product specifications, and external statements often benefit from this boundary.

Open brainstorming, comparison reports, decision logs, review responses, change explanations, and requests to explain why an option was rejected legitimately use discussion history. Do not remove the history that constitutes the requested deliverable. When material decisions remain unresolved, clarify them before treating a final position as approved.

## Three complementary tools

| Tool | Role | When to use |
| --- | --- | --- |
| `cleanroom-writing` skill | Repeatable drafting and audit workflow | In a host that supports skills |
| [Before writing](before-writing.md) | Standalone preventive prompts and checks | Before a multi-round writing task |
| [Inspect and repair](inspect-and-repair.md) | Standalone diagnosis and repair workflow | After leakage appears in a draft |

The preventive guide establishes an effective-state record early. The repair guide reconstructs that state, diagnoses candidate passages, and uses the user's chosen confirmation stage before applying repairs.

Discussion records preserve **why a decision was made**. The effective state records **what was decided**. The final artifact presents **what its intended reader needs to know**.
