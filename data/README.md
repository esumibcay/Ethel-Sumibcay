# Data

Sourced inputs used across engagements. Every dataset here notes its
provenance (source, date pulled, any transformations).

## Individual Research Paper (nurse turnover and retention)

| File | Source | Published / pulled | Transformations |
|---|---|---|---|
| nsi_2026_retention_report.pdf | NSI Nursing Solutions, Inc., *2026 NSI National Health Care Retention & RN Staffing Report* | Published March 2026 (covers Jan–Dec 2025); pulled [date] | None |
| nsi_turnover.csv | NSI 2026 report, p. 5 chart | Pulled [date] | Staff RN turnover rate, 2021–2025, copied by hand |
| nsi_cost.csv | NSI 2026 report, Quick Reference Guide | Pulled [date] | Cost per RN turnover and cost per 1-point change, copied by hand |
| oews_rn_2015_2019.csv | U.S. BLS, Occupational Employment Statistics, national estimates, Registered Nurses (SOC 29-1141) | May 2015–May 2018 from each year's national news release (Table 1); May 2019 from the RN occupation page; pulled [date] | Employment and median hourly wage copied by hand; annual median = median hourly × 2,080 (BLS convention); deflated to real dollars with CPI-U in the analysis |
| cpi_u_annual.csv | U.S. BLS, CPI-U, U.S. city average, all items, not seasonally adjusted (series CUUR0000SA0), "Avg" column of BLS table at bls.gov/regions/northeast/data/consumerpriceindex_us_table.htm | Pulled [date] | Annual averages; used to deflate OEWS wages (2015–2019) and to convert Silvestre et al. (2017) costs from 2013 to 2025 dollars. October 2025 was not collected due to the 2025 lapse in appropriations; the BLS-published 2025 average is used as given |

Cited estimates (not raw series): Silvestre et al. (2017) program cost and
turnover rates; Aiken et al. (2002) staffing–mortality effect. Full citations
are in `capabilities/economic-research/spec.md`.
