# Playwright plan

## Why automate
The 12-row price matrix and its stacking rules are deterministic and repeat on every release. A script never skips a row. Visual and clinical judgement (charting feel, photo quality) stays manual.

## Why an oracle
Checking "a discount is shown" would pass with a wrong amount. The oracle (`oracle.py`) computes the **exact** expected charge with decimal arithmetic and a stated rounding rule, so the test compares amounts to the cent.

## Checks
| ID | What it checks | Technique |
|----|----------------|-----------|
| A01 | 12 combinations of customer x tier match the oracle | Data-driven loop over a table |
| A02 | Boundary: tier changes exactly at 2, 3 and 4 syringes | Parametrized test |
| A03 | Rebooking inside the window adds 5%; outside does not | Fake the clock with `page.clock` |
| A04 | A 100% coupon gives $0.00 and still reaches the payment step | Assert the charge request exists |
| A05 | Declined card shows a message and does not advance | `page.route()` forces a failure |
| A06 | Amount on the approval screen equals the amount sent to the payment API | Read the request body with `page.route()` |
| A07 | Mobile viewport shows the same amounts | Mobile project, iPhone 13 preset |

## Practical notes
- Use `data-testid` attributes; ask developers to add them if missing.
- Run the oracle first in CI; if it fails, the expected data is wrong and UI tests would be meaningless.
- Sensitive data: use fictitious patients and the gateway's published test cards only.
- Each test builds its own cart; no test depends on another.
