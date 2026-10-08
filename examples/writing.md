# Worked examples / 应用示例

These synthetic examples illustrate intended behavior; they are not recorded model evaluation results.

以下为合成示例，用于说明预期行为，不代表已经执行的模型评估结果。

## 1. Discarded schedule / 废弃的安排

**Conversation / 讨论：** Consider weekly reports. Reject that option. Approve monthly reports on the first business day. The reader needs only the schedule.

**Prompt:** “Use $cleanroom-writing to write the final reporting policy.”

**Expected artifact:** “Reports are delivered monthly on the first business day.”

**中文交付：** “报告于每月第一个工作日交付。”

The rejected weekly schedule and reasons for rejecting it stay out of the artifact. They remain available only as audit context.

废弃的周报安排及其取舍理由仅用于审计，不进入定稿。

## 2. Necessary limitation / 必要限制

**Approved requirement / 已确认要求：** The tool processes local files. It must not upload source documents. Readers need to know that restriction.

**Expected artifact:** “The tool processes local files and must not upload source documents.”

**中文交付：** “工具处理本地文件，不得上传源文档。”

The negative statement communicates an effective requirement and must remain.

否定句表达有效要求，应当保留。

## 3. Chinese discussion, English output / 中文讨论、英文成稿

**讨论：** “之前的草稿写了每周一次，最终定为每月一次。请用英文写最终安排，不介绍修改经过。”

**Expected artifact:** “Reports are delivered monthly.”

The requested English output takes precedence over the discussion language.

交付语言遵循用户指定的英文。

## 4. Unresolved decision / 未决事项

**Conversation / 讨论：** “We considered monthly and quarterly reports, but have not chosen either. Write the final policy.”

**Expected behavior:** Ask which interval is approved, or leave that detail unresolved if the user permits a partial draft. Do not invent an approved schedule.

**预期行为：** 澄清交付周期，或在用户允许部分草稿时保留未决项，不自行确定周期。

## 5. Requested comparison / 明确要求比较

**Request / 请求：** “Explain why we chose monthly reports over weekly reports for the decision log.”

**Expected behavior:** Preserve the requested comparison and reasons. The decision history is part of this deliverable.

**预期行为：** 保留要求的比较与理由，决策历史是该交付物的内容。

## 6. Synchronize a revision / 同步修订

**Approved change / 已确认修改：** The reporting interval changed from weekly to monthly. The body, abstract, and a table still contain different intervals.

**Expected behavior:** Apply monthly reporting to all relevant locations, then audit for obsolete intervals and internal revision explanations. Do not insert “changed from weekly” into the final policy solely to describe the edit.

**预期行为：** 将正文、摘要和表格统一为月度安排，检查旧周期残留，并避免把修改过程写进最终制度。
