# Approach

## Scope
In: booking estimate, checkout discount engine, treatment planning and approval, complement funnel, rebooking, coupons, product tracking (lot/expiry), facial charting persistence, final documentation, payment, inventory dropdown, cross-platform consistency.
Out: marketing pages, push-notification delivery, payment gateway internals.

## Standards
- ISO/IEC/IEEE 29119-2 (test processes), -3 (documentation), -4 (techniques)
- ISTQB CTFL 4.0 (techniques, risk-based testing, exploratory testing)

## Deliverables (as spreadsheets in the original work, as Markdown here)
Test Plan, Schedule, Risk Register, Entry/Exit criteria; Test Conditions; Decision Table and price calculator; Test Cases, Charters, Coverage Items, Test Data and Environment requirements; Test Sets and Procedures, execution schedule; Defect Report template (29119-3, 11 fields).

## Process
1. **Analysis:** 48 test conditions in 12 feature sets, each with source technique, priority, linked risk and requirement.
2. **Design:** 31 test cases, 5 charters, 39 coverage items.
3. **Implementation:** 13 test sets with ordered procedures, instantiated test data, a 2-day execution schedule with buffer for retests.
4. **Execution and reporting** (not shown): defects logged with severity and priority definitions.

## Key assumptions that were resolved early
| # | Assumption | How it was settled |
|---|------------|--------------------|
| A1 | Do the member discount and the volume discount add up, or multiply? | Confirmed with a real worked example: they multiply, no cap |
| A2 | In which order do rebooking and coupon apply? | Rebooking on the volume-discounted value, coupon last |
| A3 | Does a 100% coupon skip payment? | No: a $0.00 charge is processed normally |
| A4 | Can extra syringes be added in the original funnel? | No: only through the complement funnel |

## Lessons learned
- A formula written in a requirements document is a hypothesis until a **worked numeric example** confirms it. One example (3 syringes = $1,800) closed an ambiguity that prose could not.
- Ask for the order of composition as soon as three or more adjustments can coexist.
- Money tests need an oracle with exact decimal arithmetic and an explicit rounding rule.
