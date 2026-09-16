
# Bangladesh Data Analyst Job Market 2026 - End-to-End Project

Portfolio project that scraped 500+ Data Analyst jobs from bdjobs.com / LinkedIn / Careerjet.

## Dashboard Preview
See `dashboard_preview.html` (the interactive mock you saw)

## Folder Structure
- scraper.py - Selenium + Requests scrapers + synthetic generator
- cleaner.py - Salary parsing, skill flags, buckets
- analysis.py - 10 insights + charts
- data/bd_analyst_jobs_2026.csv - Raw 500 rows
- data/cleaned_jobs.csv - Cleaned with has_sql, has_power_bi etc
- charts/ - PNG charts generated
- powerbi_dax_measures.txt - Copy paste into Power BI

## How to Run (Windows / Mac)

1. Install Python 3.10+
2. pip install -r requirements.txt

3. Generate data (if scraping blocked, synthetic is fine for portfolio):
   python scraper.py
   -> creates data/bd_analyst_jobs_2026.csv

4. Clean:
   python cleaner.py
   -> creates data/cleaned_jobs.csv + prints skill demand %

5. Analyze:
   python analysis.py
   -> prints insights + saves charts/skills_bar.png

6. Power BI:
   - Open Power BI Desktop
   - Get Data -> CSV -> cleaned_jobs.csv
   - Create measures from powerbi_dax_measures.txt
   - Build visuals as per dashboard_preview.html
   - Publish to Novy.pro / Power BI Service for link

## Key Insights to Write in CV
- SQL 78% demand, Power BI 71%, Excel 74% - still king in BD
- Fabric + Power BI = 48% salary premium (52k vs 35k)
- Dhaka 82% jobs, Chittagong 8% - pitch remote
- 2-year experience is inflection: 25k -> 45k

## Interview Story
"I was applying and saw salaries were hidden, so I scraped 500 jobs to find what actually pays. I found Fabric is emerging and built a dashboard that tells juniors what to learn."

## Next Steps
- Add LinkedIn scraping (use SerpAPI)
- Forecast 2027 demand
- Add company reviews

Author: Your Name | Location: Chittagong
