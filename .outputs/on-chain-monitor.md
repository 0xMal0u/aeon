## Summary

**on-chain-monitor run — 2026-10-04**
Watch: `BaseHouse Subscriptions` — `0xeE2E5506c6194d02e86767d3e88bE786D39f9463` on Base

**Data sources:**
- Etherscan v2 keyless → failed (Base not supported on free tier)
- Basescan.org → 403
- BlockScout REST API → success (full transaction history)
- Base public RPC → success (current block + recent logs)

**Scan result:** `ON_CHAIN_OK`
- Current block: 52,167,093
- Scan window: blocks 52,165,094 → 52,167,093 (~67 min, 1,999 blocks)
- Raw events: 0 | Kept: 0 | No notification sent

**Historical context found (pre-monitor baseline):**
| Date | Amount | Plan | From | Tx |
|------|--------|------|------|----|
| 2026-06-11 19:45 UTC | $5 USDC | Builder ($5/mo) | 0xa1B43C1…b33 | `0x00b294…` |
| 2026-06-11 21:24 UTC | $15 USDC | Pro ($15/mo) | 0xa1B43C1…b33 | `0xb997f2…` |

Same address subscribed twice (likely testing/upgrading). Contract has been dormant since June 12, 2026.

**Files created:**
- `memory/on-chain-watches.yml` — watch config for BaseHouse subscription contract
- `memory/on-chain-state.json` — state initialized at block 52,167,093
- `memory/logs/2026-10-04.md` — run log with full historical context

Future runs will scan from block 52,167,093 forward and notify on any new subscription payments.
