"""Pricing oracle for a filler (injectable) checkout with stacked discounts.

Rules (synthetic, modelled on a real marketplace feature):
  unit price   = regular price, or 75% of it for New Client / Plus members
  volume tier  = 1 syringe 0%, 2 -> 15%, 3 -> 20%, 4+ -> 25%
  final value  = unit x qty x (1 - volume)            (discounts COMPOUND, no cap)
  rebooking    = extra 5% on the already-discounted value
  coupon       = last layer, applied on the value after all other discounts
  complement   = extra syringes bought later; the volume tier uses the
                 ACCUMULATED count (original + complement)
Money is rounded half-up to cents after every step that is shown to a user.
Run:  python3 -I automation/oracle.py
"""
import csv
import os
import sys
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
MEMBER_FACTOR = Decimal("0.75")
TIERS = [(4, Decimal("0.25")), (3, Decimal("0.20")), (2, Decimal("0.15")), (1, Decimal("0"))]


def money(x):
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def volume_discount(qty):
    for minimum, rate in TIERS:
        if qty >= minimum:
            return rate
    raise ValueError("qty must be >= 1")


def unit_price(regular, customer):
    regular = Decimal(regular)
    return money(regular * MEMBER_FACTOR) if customer in ("New Client", "Plus") else money(regular)


def final_value(regular, customer, qty, already_bought=0, rebooking=False, coupon_pct=Decimal("0")):
    """Value charged for `qty` syringes. `already_bought` = syringes in the original funnel."""
    unit = unit_price(regular, customer)
    rate = volume_discount(qty + already_bought)
    value = money(unit * qty * (1 - rate))
    if rebooking:
        value = money(value * Decimal("0.95"))
    if coupon_pct:
        value = money(value * (1 - Decimal(coupon_pct) / 100))
    return value


def load_products():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "pricing_oracle.csv")
    with open(path, newline="") as f:
        return {r["product"]: Decimal(r["regular_price"]) for r in csv.DictReader(f)}


# Expected values worked out by hand in test-design/decision-table.md
CHECKS = [
    # (description, args, expected)
    ("Regular x1",  dict(customer="Regular", qty=1), "1000.00"),
    ("Regular x2",  dict(customer="Regular", qty=2), "1700.00"),
    ("Regular x3",  dict(customer="Regular", qty=3), "2400.00"),
    ("Regular x4",  dict(customer="Regular", qty=4), "3000.00"),
    ("New Client x1", dict(customer="New Client", qty=1), "750.00"),
    ("New Client x2", dict(customer="New Client", qty=2), "1275.00"),
    ("New Client x3", dict(customer="New Client", qty=3), "1800.00"),
    ("New Client x4", dict(customer="New Client", qty=4), "2250.00"),
    ("Plus x1",     dict(customer="Plus", qty=1), "750.00"),
    ("Plus x2",     dict(customer="Plus", qty=2), "1275.00"),
    ("Plus x3",     dict(customer="Plus", qty=3), "1800.00"),
    ("Plus x4",     dict(customer="Plus", qty=4), "2250.00"),
    ("Plus x5 (4+ tier holds)", dict(customer="Plus", qty=5), "2812.50"),
    ("Plus x4 + rebooking", dict(customer="Plus", qty=4, rebooking=True), "2137.50"),
    ("Plus x4 + rebooking + 10% coupon", dict(customer="Plus", qty=4, rebooking=True, coupon_pct=10), "1923.75"),
    ("Plus x3 + 100% coupon", dict(customer="Plus", qty=3, coupon_pct=100), "0.00"),
    ("Complement: 2 original + 2 more -> 25% tier", dict(customer="Plus", qty=2, already_bought=2), "1125.00"),
]


def main():
    products = load_products()
    regular = products["Filler A"]
    failures = 0
    for desc, args, expected in CHECKS:
        got = final_value(regular, **args)
        ok = got == Decimal(expected)
        failures += not ok
        print(f"{'OK  ' if ok else 'FAIL'} {desc:<46} expected {expected:>9} got {got:>9}")
    # rounding rule: member price of Filler C is 250.005 -> 250.01 (half-up)
    c = products["Filler C"]
    got = final_value(c, "Plus", 3)
    ok = unit_price(c, "Plus") == Decimal("250.01") and got == Decimal("600.02")
    failures += not ok
    print(f"{'OK  ' if ok else 'FAIL'} {'Rounding: Filler C Plus x3 (250.01 x 3 x 0.80)':<46} expected    600.02 got {got:>9}")
    total = len(CHECKS) + 1
    print(f"{total - failures} of {total} checks OK")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
