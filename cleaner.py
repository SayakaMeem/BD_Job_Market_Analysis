
import pandas as pd
import re

df = pd.read_csv("data/bd_analyst_jobs_2026.csv")

# Clean salary
df["salary_min"] = pd.to_numeric(df["salary_min"], errors="coerce")
df["salary_max"] = pd.to_numeric(df["salary_max"], errors="coerce")
df["salary_avg"] = (df["salary_min"] + df["salary_max"])/2

# Skill flags - THIS IS YOUR ANALYST LOGIC
skills = ["SQL", "POWER BI", "EXCEL", "PYTHON", "TABLEAU", "FABRIC", "ETL", "DASHBOARD", "STATISTICS"]
for skill in skills:
    col = f"has_{skill.lower().replace(' ', '_')}"
    df[col] = df["skills_raw"].str.upper().str.contains(skill).astype(int)

# Location normalization
df["location"] = df["location"].str.title()

# Experience bucket
def bucket_exp(x):
    if x <=1: return "Fresher (0-1)"
    elif x <=3: return "Mid (2-3)"
    else: return "Senior (4+)"
df["exp_bucket"] = df["experience_years"].apply(bucket_exp)

# Salary bucket
def bucket_sal(x):
    if pd.isna(x): return "Negotiable"
    if x <25000: return "15-25k"
    if x <35000: return "25-35k"
    if x <50000: return "35-50k"
    if x <70000: return "50-70k"
    return "70k+"
df["salary_bucket"] = df["salary_avg"].apply(bucket_sal)

df.to_csv("data/cleaned_jobs.csv", index=False)
print("Cleaned -> data/cleaned_jobs.csv")
print(df[["has_sql","has_power bi","has_python"]].mean().sort_values(ascending=False)*100)
