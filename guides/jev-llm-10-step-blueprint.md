# Jev + LLMs: The 10-Step Blueprint

**Source:** [@0xwhrrari](https://x.com/0xwhrrari/status/2103157617715491278) — *"Jev Founder, Diogo Almeida, just released a 12-page PDF on how to use Jev with LLMs."*
**Full PDF:** [`../PDF/Jev_How_to_Use_Jev_with_LLMs_Field_Guide.pdf`](../PDF/Jev_How_to_Use_Jev_with_LLMs_Field_Guide.pdf) — 12 pages.

A 10-step blueprint for building a faster, cheaper, more controllable AI system around Claude, Codex, Grok, or any LLM:

1. **Split the responsibilities** — the LLM generates, Jev makes bounded semantic decisions, deterministic code keeps authority.
2. **Build the state** — give Jev the current request, relevant evidence, policy, and proposed action instead of sending the entire conversation.
3. **Choose the right primitive** — Choice selects a route, Score evaluates an ordered rubric, Noul returns the probability that a statement is true.
4. **Replace giant evaluation prompts with atomic questions** — intent, urgency, evidence, risk, and scope become separate typed decisions.
5. **Put Jev before the LLM** — select the context, tools, provider, and workflow before paying for an expensive generative call.
6. **Give the LLM a bounded job** — once Jev selects the route, the model receives only the instructions, files, and tools required for that branch.
7. **Put Jev after the LLM** — check whether the result answers the request, uses sufficient evidence, and stays inside the permitted scope.
8. **Route by confidence** — high-confidence low-risk cases proceed automatically, uncertain cases request more context, consequential actions go to review.
9. **Batch independent decisions** — ask multiple Choice, Score, and Noul questions over one shared state instead of creating another LLM call for every judgment.
10. **Record the complete decision receipt** — state version, question, probabilities, selected route, model, latency, outcome, and human override.

The point: most AI courses teach you to write a bigger prompt. This teaches you to build the control system around every prompt. Result: smaller contexts, fewer unnecessary LLM calls, safer tool execution, and decisions you can inspect, test, and improve.

Quoted thread: "Most AI agents waste tokens on decisions that never needed text. Jev turns routing, scoring, and verification into a fast decision layer."

Related X article: https://x.com/i/article/2101963175180582912
