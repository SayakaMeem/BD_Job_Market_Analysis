
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/cleaned_jobs.csv")

print("=== BD DATA ANALYST MARKET 2026 ===")
print(f"Total Jobs: {len(df)}")
print(f"Avg Salary (disclosed): {df['salary_avg'].mean():.0f} BDT")
print(f"Salary disclosure rate: {df['salary_avg'].notna().mean()*100:.1f}%")

# Q1 Top Skills
skill_cols = [c for c in df.columns if c.startswith("has_")]
skill_rate = df[skill_cols].mean().sort_values(ascending=False)*100
print("\nTop Skills:\n", skill_rate)

# Q2 Dhaka vs CTG
print("\nLocation vs Avg Salary:\n", df.groupby("location")["salary_avg"].agg(["count","mean"]))

# Q3 Experience vs Salary
print("\nExp Bucket vs Salary:\n", df.groupby("exp_bucket")["salary_avg"].mean())

# Q4 Fabric premium
fabric_premium = df.groupby("has_fabric")["salary_avg"].mean()
if len(fabric_premium)>1:
    print(f"\nFabric Premium: {fabric_premium.iloc[1]/fabric_premium.iloc[0]*100-100:.0f}% higher")

# Save charts
plt.figure()
skill_rate.plot(kind="barh")
plt.title("Top Demanded Skills - BD Data Analyst")
plt.tight_layout()
plt.savefig("charts/skills_bar.png", dpi=200)

plt.figure()
df["salary_bucket"].value_counts().reindex(["15-25k","25-35k","35-50k","50-70k","70k+","Negotiable"]).plot(kind="bar")
plt.title("Salary Distribution BD")
plt.tight_layout()
plt.savefig("charts/salary_dist.png", dpi=200)

print("\nCharts saved to /charts")
