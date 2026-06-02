import pandas as pd
import os
from pathlib import Path

RAW_FOLDER = Path("data/raw")
print("="*80)
print("MUTUAL FUND DATA INGESTION")
print("="*80)

csv_files = list(RAW_FOLDER.glob("*.csv"))
summary = []

for file in csv_files:

    print("\n")
    print("="*80)
    print(f"FILE : {file.name}")
    print("="*80)

    try:

        df = pd.read_csv(file)

        print("\nShape")
        print(df.shape)

        print("\nColumns")
        print(df.columns.tolist())

        print("\nData Types")
        print(df.dtypes)

        print("\nTop 5 Rows")
        print(df.head())

        print("\nMissing Values")
        print(df.isnull().sum())

        print("\nDuplicate Rows")
        print(df.duplicated().sum())

        summary.append({
            "file": file.name,
            "rows": df.shape[0],
            "columns": df.shape[1],
            "missing_values": int(df.isnull().sum().sum()),
            "duplicates": int(df.duplicated().sum())
        })

    except Exception as e:

        print(f"Error : {e}")

summary_df = pd.DataFrame(summary)

summary_df.to_csv(
    "data/processed/data_quality_summary.csv",
    index=False
)
print("\nData Quality Summary Saved")