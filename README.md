# QA Portfolio: Filler Checkout and Discount Engine (Testware #001)

An anonymized showcase of how I planned and designed the tests for a **pricing and discount overhaul** in a health & aesthetics services marketplace: per-syringe pricing, member prices, volume tiers, rebooking and coupons, across web, customer app, provider app and admin. It follows ISO/IEC/IEEE 29119 and ISTQB CTFL 4.0. No internal company data, names or links are included, and all prices are synthetic.

## What this is

The feature replaced fixed "packages" with a price per syringe plus stacked discounts. Money rules look simple, but they hide many edge cases (compounding, tier boundaries, rounding, late add-ons, coupons), which makes them a good subject for systematic test design.

## Rules under test

| # | Rule |
|---|------|
| D1 | Member price (New Client / Plus) = 75% of the regular price |
| D2 | Volume tiers: 1 syringe 0%, 2 = 15%, 3 = 20%, 4+ = 25% |
| D3 | Discounts **compound** (multiply); there is no cap |
| D4 | Rebooking: extra 5% on the already-discounted value, only inside a same-day time window |
| D5 | Coupon is the **last** layer, applied after all other discounts |
| D6 | A complement funnel (extra syringes) uses the **accumulated** count to pick the tier, and creates its own charge |
| D7 | A partially used syringe counts as a whole one |

## Repository map

| Path | Content |
|------|---------|
| `docs/approach.md` | Scope, standards, techniques, assumptions, schedule, lessons learned |
| `test-design/decision-table.md` | 12 combinations (3 customer types x 4 tiers) plus stacking rules |
| `test-design/test-cases.md` | 31 test cases grouped by feature set, with technique and traceability |
| `test-design/risk-register.md` | Product and project risks, scored and mitigated |
| `test-design/charters.md` | 5 exploratory session charters |
| `data/pricing_oracle.csv` | 3 synthetic products, including a fractional price |
| `automation/oracle.py` | Computes the expected charge and self-checks 18 scenarios |
| `automation/playwright-plan.md` | Plan for data-driven price checks |
| `automation/tests/pricing.spec.ts` | Skeleton spec with placeholders |

## Test design techniques used

- **Decision table:** customer type x syringe tier, plus rebooking and coupon layers.
- **Boundary value analysis:** 1/2/3/4/5 syringes; rebooking at the edge of the time window; a 100% coupon ($0.00 charge).
- **Equivalence partitioning:** customer types, valid and invalid coupons.
- **State-based testing:** estimate -> approval -> token -> charge; original funnel -> complement funnel.
- **Error guessing:** compounding instead of a cap, partially used syringes, cent rounding, second coupon.
- **Exploratory charters:** charting persistence, upload on a poor network, combinations outside the table.

## Running the oracle

Requires Python 3.9 or later. No packages to install.

```bash
python3 -I automation/oracle.py
```

Expected end of output: `18 of 18 checks OK`.

The oracle uses `Decimal` with half-up rounding to the cent, so it cannot drift the way floating point does. A UI test compares the price shown on screen against it, so the test checks the **exact amount**, not just that a discount exists.

## Skills shown

Test planning and estimation, risk-based testing, decision tables, boundary analysis, test data design, oracle thinking, money and rounding pitfalls, traceability from requirement to condition to case, and a first step into UI test automation.

## Status

Design and planning are complete. Execution results are not included because the target application is private.
