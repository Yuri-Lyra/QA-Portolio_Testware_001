# Exploratory charters (session-based)

| ID | Mission | Timebox | Risks | Observe |
|----|---------|---------|-------|---------|
| CT01 | Explore facial charting with the maximum number of points, lines and combinations to find loss or corruption of clinical data | 60 min | R5 | Data loss on save/reopen; behavior at large point counts; session drop mid-fill |
| CT02 | Explore photo and video upload under slow, intermittent or lost connection | 45 min | R8 | Error clarity; lost form data; retry; very large files |
| CT03 | Explore the discount engine outside the official table: 0 syringes, 10+ syringes, changing customer type mid-flow, back-and-forth before approval | 45 min | R1, R10 | Any amount that differs from the oracle; estimate vs checkout desync |
| CT04 | Explore rebooking, coupon and complement funnel combined to find undocumented composition orders | 45 min | R3, R14, R15 | Real order of application; rounding drift when 3+ adjustments coexist |
| CT05 | Watch the admin in real time while actions happen in the customer and provider apps | 30 min | R10 | Sync delay; inconsistent state when an action fails midway |

Each session ends with a short note: what was covered, what was found, what to do next.
