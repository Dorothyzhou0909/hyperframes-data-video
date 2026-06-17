# Financial Verification

Use this reference for public-company financial videos, investor-report explainers, annual/quarterly report summaries, and any data that could affect financial interpretation.

## Source Priority

Prefer primary sources:

1. Company annual reports, quarterly reports, investor presentations, and official announcements.
2. Exchange filings and regulatory disclosure platforms.
3. Audited financial statements and notes.
4. Reputable data aggregators only as secondary cross-checks.

When data may have changed recently, browse and cite sources. Use exact report dates and periods.

## Data Handling

- Normalize all monetary values to one unit, usually RMB 100M / 人民币亿元 for Chinese companies.
- Preserve decimals intentionally: use 0 decimals for large annual revenue, 1 decimal for quarter data if needed, 2 decimals for percentages when the source uses them.
- Separate source data from display code in `data.js`, JSON, CSV, or a similar config.
- Keep derived metrics explainable. If deriving ratios or differences, make them traceable to source values.
- Use "unaudited" labels for quarterly reports if the source says quarterly figures are unaudited.

## Narrative Discipline

- Balance growth drivers and pressure points.
- Do not add stock price, valuation, or investment forecasts unless the user asks and sources support it.
- Avoid "beat/miss" language unless there is a verified analyst expectation source.
- End with a source line. Add "不构成投资建议" or equivalent when the video involves listed companies, financial performance, investment interpretation, or market-sensitive data.

## Final Checks

Before final render, check:

- Every final number matches the chosen source and unit.
- Year/quarter labels are correct.
- Percent changes and percentage-point changes are not mixed up.
- Downturns are not visually framed as gains.
- Source note is visible long enough to read.
