import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

returns_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in returns_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

anomalies = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("Expense Ratio Anomalies")
print(anomalies)

df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("Scheme performance cleaned")