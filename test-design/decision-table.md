# Decision table: checkout discount

Final value = unit price x quantity x (1 - volume discount). Example product: regular $1,000 (member price $750).

| # | Customer | Syringes | Volume | Unit | Subtotal | Final value |
|---|----------|----------|--------|------|----------|-------------|
| 1 | Regular | 1 | 0% | $1,000 | $1,000 | $1,000.00 |
| 2 | Regular | 2 | 15% | $1,000 | $2,000 | $1,700.00 |
| 3 | Regular | 3 | 20% | $1,000 | $3,000 | $2,400.00 |
| 4 | Regular | 4+ | 25% | $1,000 | $4,000 | $3,000.00 |
| 5 | New Client | 1 | 0% | $750 | $750 | $750.00 |
| 6 | New Client | 2 | 15% | $750 | $1,500 | $1,275.00 |
| 7 | New Client | 3 | 20% | $750 | $2,250 | $1,800.00 |
| 8 | New Client | 4+ | 25% | $750 | $3,000 | $2,250.00 |
| 9 | Plus | 1 | 0% | $750 | $750 | $750.00 |
| 10 | Plus | 2 | 15% | $750 | $1,500 | $1,275.00 |
| 11 | Plus | 3 | 20% | $750 | $2,250 | $1,800.00 |
| 12 | Plus | 4+ | 25% | $750 | $3,000 | $2,250.00 |

Compounding insight: a member with 4+ syringes pays 0.75 x 0.75 = 56.25% of retail, a total discount of **43.75%**, not 25%.

## Stacking layers (applied in this order)
1. Member price (unit price)
2. Volume tier (by accumulated syringe count)
3. Rebooking, 5% (same-day window only)
4. Coupon (last)

| Scenario | Calculation | Result |
|----------|-------------|--------|
| Plus, 4 syringes, rebooking | 2,250.00 x 0.95 | $2,137.50 |
| Plus, 4 syringes, rebooking, 10% coupon | 2,137.50 x 0.90 | $1,923.75 |
| Plus, 3 syringes, 100% coupon | 1,800.00 x 0 | $0.00 (charge still processed) |
| Complement: 2 original + 2 more | 2 x 750 x 0.75 | $1,125.00 (25% tier, not 15%) |
| Rounding: member price 250.005 -> 250.01; 3 syringes | 250.01 x 3 x 0.80 | $600.02 |
