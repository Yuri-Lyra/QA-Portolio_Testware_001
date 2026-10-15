# Risk register

Likelihood (L) and impact (I) on a 1 to 5 scale. Score = L x I. Levels: 15+ High, 8-14 Medium, below 8 Low.

| ID | Type | Risk | L | I | Score | Level | Mitigation |
|----|------|------|---|---|-------|-------|------------|
| R1 | Product | Member discount and volume discount combined differently than intended | 5 | 5 | 25 | High | Confirm the formula with a worked example before fixing expected values; decision table with 12 combinations |
| R10 | Product | Discount logic differs across web, apps and admin | 4 | 5 | 20 | High | Run the same table on every platform separately |
| R11 | Project | Short deadline for a feature touching payment, inventory, charting and 4 platforms | 4 | 4 | 16 | High | Execute by risk score; raise a renegotiation early |
| R3 | Product | Complement funnel ignores the accumulated syringe count | 3 | 5 | 15 | High | 2 + 2 syringes must land in the 25% tier |
| R4 | Product | Duplicate or missing token or charge in the complement funnel | 3 | 5 | 15 | High | One traceable charge per funnel; check idempotency on resubmit |
| R5 | Product | Facial charting not persisted (clinical and legal risk) | 3 | 5 | 15 | High | Exploratory charter; reopen the record after saving |
| R9 | Product | Old package bookings display or charge wrongly after rollout (no migration) | 3 | 4 | 12 | Medium | Read-only checks on old bookings |
| R8 | Product | Mandatory upload freezes on a poor network | 3 | 3 | 9 | Medium | Throttled-network test; retry without losing form data |
| R12 | Project | New rule ambiguities appear during execution | 3 | 3 | 9 | Medium | Fast channel with backend and frontend owners |
| R2 | Product | Partially used syringe excluded from the tier count | 2 | 4 | 8 | Medium | Dedicated boundary case |
| R6 | Product | Cent rounding differs between screens and gateway | 3 | 2 | 6 | Low | Compare displayed, charged and stored amounts; fractional-price product |
| R7 | Product | Inventory dropdown out of sync with the price table | 2 | 3 | 6 | Low | Parity checklist for each new product |
| R13 | Project | Sensitive test data (fictitious patient and card) not ready in time | 2 | 3 | 6 | Low | Prepare and validate data before execution starts |
| R14 | Product | Rebooking window or order of composition wrong | 3 | 4 | 12 | Medium | Time-boundary cases; confirm the order of layers |
| R15 | Product | Coupon order relative to volume and rebooking | 3 | 4 | 12 | Medium | Assumed last layer, later confirmed and closed |

Lesson: a risk marked "Mitigated" needs a named test or confirmation behind it, not just a plan.
