# Megabrain (Jev) & Six Grok Bots — Setup Guide

**Source:** [@savipww](https://x.com/savipww) — *"Megabrain (Jev) & Six Grok Bots That Already Made Me Six Figures (Setup Guide)"*
**Published:** September 23, 2026
**Article:** https://x.com/savipww/article/2102720919185617314

> Archived summary for reference. The "six figures" claim is the author's, not independently verified. His own disclaimer: *"This is my setup, not your strategy! Copy the shape, not the constants! NFA and Always DYOR!"*

## The concept

An upgrade to the author's earlier Grok Bot trading desk guide. Every judgement on the desk is now a **typed number with a probability** (via the Jev decision model, nicknamed "Megabrain") instead of prose the code had to parse.

A collector pulls every FOMO token with its metrics, the chain data for its chain, and the project's X account. Jev answers typed questions about each one, then makes one final call — which token to trade — and the Grok Bot desk trades it.

Author's advice: *"PASTE THIS ENTIRE GUIDE INTO YOUR CODING AGENT AND TELL IT TO BUILD THE DESK."*

## Six prerequisites

1. **A Jev key** — TypeSafe ([console.typesafe.ai](https://console.typesafe.ai)). Jev generates no text; you send state + typed questions, get typed answers with probabilities in 70–500ms. Model `jev-latest` (observed `jev-1.13.0`), $0.042/Mtok input, output free. Limits: 250k tok/sec, 1200 req/min, 64k context. **Only the judge service holds this key; no bot ever sees it.**
2. **The three question types** — the entire API: `noul` (is this true → 0–1 probability), `choice` (which one, up to 255 options → choice + probabilities + confidence), `score` (rate on a rubric, up to 10 levels). *"Noul is an if, choice is a switch, score is a sort."*
3. **The SDK** — `pip install typesafe-sdk` (Python 3.10+); provides `AsyncTypeSafeClient` and `Choice`, `Noul`, `Score` classes.
4. **A FOMO session** — FOMO has no public API; the collector reads your logged-in Chrome session (Privy bearer via CDP, ~1 hour lifetime, client refreshes it). `POST prod-api.fomo.family/proxy/filterTokens` with 20 tokens per call. Chain netIds: Solana 1399811149, Robinhood 4663, BSC 56, Base 8453, ETH 1, Monad 143.
5. **Chain data** — GeckoTerminal (free, 10 calls/min — the rate limit that shapes the whole funnel), Solana RPC (free, `getTokenLargestAccounts`, `getTokenSupply`), Etherscan V2 (one key, 60+ chains via `?chainid=`; PRO fields don't cover Solana or Robinhood).
6. **The desk itself** — the Grok Bot seats from the original guide; fills go only through FOMO ([referral](https://fomo.family/r/savipww)).

## The funnel (stages 0–6)

| Stage | Name | What happens |
|---|---|---|
| 0 | UNIVERSE | GeckoTerminal new_pools on 3 chains → fresh launches |
| 1 | LIST | FOMO filterTokens, 20/call → hundreds in one batch |
| 2 | FREE CUT | Age, liquidity, volume, mcap, no network → tens |
| 3 | TRADE CUT | DexScreener buys/sells, one call per token → a handful |
| 4 | DOSSIER | GeckoTerminal info + chain RPC + X → 3 per cycle |
| 5 | JUDGE | Market + chain + social questions per token → scored shortlist |
| 6 | PICK | One choice over the shortlist → one token or none |

## How Jev ("Megabrain") fits

Jev is the **judge, not a trader**. One service (`judge.py`, a FastAPI app) holds the only Jev API key; bots get a separate `DESK_SECRET` and call `POST $JUDGE_URL` with `{"question_set": "<market|solana|bsc|robinhood|social|pick>", "state": {...}}`. Answers come back raw with model id — never thresholded at the judge.

*"Jev takes the judgements. Code takes the arithmetic. Every number on the desk is computed before the call and passed in as a field."*

Key rules: one call per token (never one per question); state is a named object, not a blob; thresholds don't transfer between primitives; log the model id; never retry 422.

*"Jev picks what to hold. Grok Bot decides how much and how long. The exit rule answers to neither of them."*

## The six bot seats

- **SCAN** — runs `universe()` and `shortlist()`: fresh pools → normalized tokens → free-filtered, turnover-ranked queue.
- **VET** — builds the dossier: GeckoTerminal token info + chain RPC data (top wallet on Solana) + normalized X handle.
- **SOCIAL** — a prompt pasted into the bot. Uses Grok Bot's own X plugin to read the project's X account into named fields (handle, created_at, followers, posts, recent posts with replies/reposts, handle_history, bio, linked_site), then posts question_set "social" to the judge. *"Grok reads, Jev judges."* Never summarizes posts, never searches for the account (handle comes off chain).
- **CHIEF** — runs `pick.py`; the only call that ever sees more than one token. Drops the order JSON into the desk channel, logs order id + model id + every answer, reports to Telegram.
- **SIZE** — position sizing: `ticket = kelly(edge) × bank` clamped at 6% of book (free cash only) × size_factor from the pick (0.40 if Robinhood "dark" data, 0.60 if no usable X account, stackable) = `min(ticket, liquidity_usd × 0.02)`; below fee floor → 0.
- **FILLS** — `effective_fee = max(0.0045 × ticket, 0.95)/ticket`; over max → FEE_FLOOR, don't send; one market order through FOMO, no ladders; slippage over max → complete and flag loudly; never sell into a distributing whale.
- **RISK** — the exit seat: `avg_6h = volume.h24/4`; `ratio = volume.h6/avg_6h`; ratio < 0.20 → CLOSE fully within 60 seconds; polls every 5 min; calls `book.release()` when the close fills. *"One rule, no conversation, final authority, nobody overrules it."*

## Question sets (questions.py)

- **MARKET** — shape / liquidity_fits_ticket / momentum_already_spent
- **CHAIN_SOLANA** — authority_risk / concentration_is_exit_risk / dev_still_loaded
- **CHAIN_BSC** — sell_side_risk / concentration_is_exit_risk / pool_quality
- **CHAIN_ROBINHOOD** — data_coverage / sellable_by_evidence / concentration_is_exit_risk / dev_still_loaded
- **SOCIAL** — account_is_the_project / audience_is_real / recycled_account / effort
- **PICK** — best + worth_trading_at_all

## Thresholds

**HARD** (filter.py): age 15 min–72 h; liq ≥ $12k; vol24 ≥ $40k; mcap $60k–$8M; trades_h24 ≥ 150; top_wallet ≤ 5% (Solana-only); top_10 ≤ 60%; holders ≥ 80.

**SOFT** (on Jev answers): concentration ≤ 0.55; momentum ≤ 0.60; liquidity_fits_ticket ≥ 0.60; account_is_the_project ≥ 0.70; recycled_account ≤ 0.50; audience_is_real ≥ 0.45; effort ≥ 1.0; dev_still_loaded ≤ 0.55; sellable_by_evidence ≥ 0.60.

Pick minimums: worth 0.60, confidence 0.55; SHAPE_MIN_CROWD 0.55; DARK_TICKET_CUT 0.40; NO_SOCIAL_CUT 0.60.

## The build order

`judge.py` → `collect.py` + `judge_client.py` → `questions.py` → `thresholds.py` + `filter.py` → the SOCIAL prompt → `pick.py` → the HANDOFF prompt (*"YOU DO NOT FORM OPINIONS ABOUT TOKENS. YOU CALL THE JUDGE."*) → SIZE/FILLS/RISK prompts → `book.py` (SQLite `desk.db`: one position at a time; bench table for rejected tokens by reason) → `main.py` (the 15-min shift cycle).

Run `shadow=True` for a week, then flip the flag.

## The bill

~10 Jev calls × ~1,400 tokens per cycle ≈ **$0.00059/cycle ≈ $0.057/day**. DexScreener and GeckoTerminal are free; the only other cost is the SuperGrok plan the bots already run on.

## Key links

- TypeSafe console (Jev keys): https://console.typesafe.ai
- Jev API: https://api.typesafe.ai/v1/systemone
- FOMO venue: https://fomo.family/r/savipww
- Original desk guide: https://x.com/savipww/status/2095171104004575708
- GeckoTerminal API: https://api.geckoterminal.com/api/v2
- DexScreener API: https://api.dexscreener.com/latest/dex/tokens
- Jev docs: https://docs.typesafe.ai

*Full paste-ready code blocks (judge.py, collect.py, questions.py, pick.py, book.py, main.py, and all six seat prompts) live in the original article.*
