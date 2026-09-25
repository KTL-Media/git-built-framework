# The Playbook Pattern

Every GIT BUILT series is built on one pattern: **a single agent supported by three files — PROCESS, TOOLBOX, PROOF.**

## The pattern

```
AGENT (the concept)
 ├── PROCESS.md  — the steps, in order, no skipped moves
 ├── TOOLBOX.md  — the tools, prompts, and resources the process needs
 └── PROOF.md    — how you know it worked, and the approval gate
```

## How a series gets built

1. **Process interview** — the concept is interrogated until the steps are explicit and ordered. If a step can't be explained simply, it isn't ready.
2. **Toolbox assembly** — every tool, prompt, template, and reference the process needs is gathered into the TOOLBOX. Nothing the process mentions is left undefined.
3. **Proof checklist** — the observable outcomes are defined up front: what "done" looks like, what "working" looks like, and the rule that nothing ships without explicit approval of the exact content.
4. **Series production** — the concept becomes the 10-slide carousel, per-slide clips, animated reel, and starter-kit PDF, all in GIT BUILT brand.
5. **Lead wiring** — the PLAYBOOK keyword flow captures the lead and delivers the kit (see `lead-capture` in `ktl-content-engine`).

## Build scripts

`build/` holds the production scripts from the flagship series — adapt per series:

- `make_slides_v2.py` — renders the 10 branded carousel slides
- `make_reel.sh` — assembles the animated reel
- `make_kit.py` — generates the starter-kit PDF

## The rule

The pattern is the product. A concept that can't survive the process interview doesn't become a series.
