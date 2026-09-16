import datetime
import random
import pandas as pd
import re
import pathlib

# Make sure data folder exists
pathlib.Path("data").mkdir(exist_ok=True)

# Load raw
df = pd.read_csv("data/bd_analyst_jobs_2026.csv")

# Clean salary
df["salary_min"] = pd.to_numeric(df["salary_min"], errors="coerce")
df["salary_max"] = pd.to_numeric(df["salary_max"], errors="coerce")
df["salary_avg"] = (df["salary_min"] + df["salary_max"]) / 2

# Fix skills_raw if missing
if "skills_raw" not in df.columns:
    df["skills_raw"] = ""
df["skills_raw"] = df["skills_raw"].fillna("").astype(str)

# Skill flags - YOUR ANALYST LOGIC (fixed names)
skills = ["SQL", "POWER BI", "EXCEL", "PYTHON", "TABLEAU", "FABRIC", "ETL", "DASHBOARD", "STATISTICS"]
for skill in skills:
    col = f"has_{skill.lower().replace(' ', '_')}" # power_bi not power bi
    df[col] = df["skills_raw"].str.upper().str.contains(skill, na=False).astype(int)

# Location normalization
if "location" in df.columns:
    df["location"] = df["location"].astype(str).str.title().str.strip()

# Experience bucket
df["experience_years"] = pd.to_numeric(df["experience_years"], errors="coerce").fillna(0)
def bucket_exp(x):
    if x <= 1:
        return "Fresher (0-1)"
    elif x <= 3:
        return "Mid (2-3)"
    else:
        return "Senior (4+)"
df["exp_bucket"] = df["experience_years"].apply(bucket_exp)

# Salary bucket
def bucket_sal(x):
    if pd.isna(x):
        return "Negotiable"
    if x < 25000:
        return "15-25k"
    if x < 35000:
        return "25-35k"
    if x < 50000:
        return "35-50k"
    if x < 70000:
        return "50-70k"
    return "70k+"
df["salary_bucket"] = df["salary_avg"].apply(bucket_sal)

# Save
df.to_csv("data/cleaned_jobs.csv", index=False)
print("✅ Cleaned -> data/cleaned_jobs.csv")
print(f"Rows: {len(df)}")

# Show skill demand
skill_cols = [f"has_{s.lower().replace(' ', '_')}" for s in skills]
print("\n📊 Skill Demand % in BD Market:")
print((df[skill_cols].mean() * 100).sort_values(ascending=False).round(1))