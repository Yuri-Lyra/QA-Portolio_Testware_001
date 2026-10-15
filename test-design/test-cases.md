# Test cases

31 cases in 12 groups. Traceability: TC = test condition. Platforms: Web, Customer App, Provider App, Admin.

| ID | Group | Objective | Technique | Expected result | Pri | Trace |
|----|-------|-----------|-----------|-----------------|-----|-------|
| CP001 | Booking | Book with a general treatment area | Equivalence partitioning | Booking advances; the area is attached to the appointment | High | TC001 |
| CP002 | Booking | Area is passed to Admin and Provider | State-based | Same area shown in both views | High | TC002 |
| CP003 | Booking | Cannot advance without an area | EP (invalid) | Continue stays disabled until one option is selected | Med | TC003 |
| CP004 | Booking | Estimate for a member | EP | Price shows 25% off retail, deposit also discounted | High | TC004 |
| CP005 | Booking | Estimate for a regular customer | EP | Full retail price, no discount | High | TC005 |
| CP006 | Discount | **Data-driven:** 12 combinations of customer x tier | Decision table | Checkout amount equals the oracle for every row | High | TC006, TC007 |
| CP007 | Discount | Leftover syringe is excluded from the tier count | Boundary | Leftover syringes are not counted | High | TC008-TC010 |
| CP008 | Discount | Tier boundaries 1->2->3->4 | Boundary value | Discount steps 0 -> 15 -> 20 -> 25%, no off-by-one | High | TC009 |
| CP009 | Discount | Rounding agrees across screen, gateway, Admin | EP | Three amounts identical to the cent | Med | TC011 |
| CP010 | Planning | Select several products in one plan | EP | Total syringe count is summed for the tier | High | TC012 |
| CP011 | Planning | Discount shown before approval | State-based | Recalculated discount visible before the customer approves | High | TC013 |
| CP012 | Planning | Token exists only after approval is requested | State-based | No token before submission; SMS lists discounts and credits | High | TC014 |
| CP013 | Planning | No "add syringe" option in the original funnel | Negative | Option does not exist | High | TC015 |
| CP014 | Tracking | Lot and expiry are optional | EP | None, some or all can be filled; flow never blocks | Med | TC016, TC017 |
| CP015 | Tracking | Tracking data persists | State-based | Values appear unchanged in Admin | Med | TC018 |
| CP016 | Charting | Full persistence of dots and lines | State-based | Every point and line reopens exactly as saved | High | TC019-TC024 |
| CP017 | Complement | Accumulated total decides the tier | Decision table | 2 original + 2 more is charged at the 25% tier | High | TC027, TC029 |
| CP018 | Complement | Own token and charge | State-based | Distinct token and charge from the original | High | TC028 |
| CP019 | Documentation | Completion blocked without mandatory photos | EP (invalid) | Step cannot advance until media is added | High | TC031, TC032 |
| CP020 | Documentation | Upload on an unstable network | Exploratory | Clear error, retry works, form not lost | Med | TC033 |
| CP021 | Payment | Approved amount equals charged amount | State-based | Identical | High | TC034 |
| CP022 | Payment | Declined test card | Negative | Clear message; flow does not advance | Med | TC036 |
| CP023 | Rebooking | Inside the same-day window | EP | Extra 5% on the volume-discounted value | High | TC042, TC044 |
| CP024 | Rebooking | Outside the window | Boundary (time) | No 5% discount | High | TC043 |
| CP025 | Coupons | 100% coupon | Boundary (extreme) | $0.00 charge processed; payment step not skipped | High | TC045, TC046 |
| CP026 | Coupons | Expired or invalid coupon | Negative | Rejected with a clear message | Med | TC047 |
| CP027 | Coupons | Second coupon in the same checkout | Negative | Blocked | Med | TC048 |
| CP028 | Inventory | New products in the order dropdown | EP | Listed next to existing products | Med | TC037, TC038 |
| CP029 | Inventory | Order with a new product | EP | Submitted and visible in Admin | Med | TC039 |
| CP030 | Cross-platform | Same combination on all platforms | Decision table | Identical amount on all four | High | TC040 |
| CP031 | Regression | Non-filler treatment flow unchanged | Regression | Works as before | Med | TC041 |

## Worked example for CP006 (one row)
Plus customer, 3 syringes of a $1,000 product: unit $750, subtotal $2,250, volume 20% -> **$1,800.00**. The oracle (`automation/oracle.py`) reproduces all 12 rows plus the stacking scenarios.
