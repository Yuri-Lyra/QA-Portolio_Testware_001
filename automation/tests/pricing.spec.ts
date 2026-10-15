import { test, expect } from '@playwright/test';

// Skeleton: replace paths and test ids with those of the real application.
// Expected values come from automation/oracle.py (regular price 1000.00).

type Row = { customer: 'Regular' | 'New Client' | 'Plus'; qty: number; expected: string };

const MATRIX: Row[] = [
  { customer: 'Regular', qty: 1, expected: '$1,000.00' },
  { customer: 'Regular', qty: 2, expected: '$1,700.00' },
  { customer: 'Regular', qty: 3, expected: '$2,400.00' },
  { customer: 'Regular', qty: 4, expected: '$3,000.00' },
  { customer: 'New Client', qty: 1, expected: '$750.00' },
  { customer: 'New Client', qty: 2, expected: '$1,275.00' },
  { customer: 'New Client', qty: 3, expected: '$1,800.00' },
  { customer: 'New Client', qty: 4, expected: '$2,250.00' },
  { customer: 'Plus', qty: 1, expected: '$750.00' },
  { customer: 'Plus', qty: 2, expected: '$1,275.00' },
  { customer: 'Plus', qty: 3, expected: '$1,800.00' },
  { customer: 'Plus', qty: 4, expected: '$2,250.00' },
];

test.describe('A01 checkout amount, 12 combinations', () => {
  for (const row of MATRIX) {
    test(`${row.customer} x ${row.qty} syringe(s)`, async ({ page }) => {
      await page.goto(`/test-login?as=${encodeURIComponent(row.customer)}`);
      await page.goto('/checkout?product=filler-a&qty=' + row.qty);
      await expect(page.locator('[data-testid="final-amount"]')).toHaveText(row.expected);
    });
  }
});

test('A05 declined card does not advance the flow', async ({ page }) => {
  await page.route('**/api/payments*', (route) =>
    route.fulfill({ status: 402, json: { error: 'card_declined' } }),
  );
  await page.goto('/checkout?product=filler-a&qty=2');
  await page.locator('[data-testid="pay-button"]').click();
  await expect(page.locator('[data-testid="payment-error"]')).toBeVisible();
  await expect(page.locator('[data-testid="confirmation"]')).toHaveCount(0);
});
