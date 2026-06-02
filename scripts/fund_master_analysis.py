import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("="*60)
print("FUND MASTER ANALYSIS")
print("="*60)

print("\nTotal Records:")
print(len(df))

print("\nUnique Fund Houses:")
print(df["fund_house"].nunique())

print(df["fund_house"].unique())

print("\nUnique Categories:")
print(df["category"].unique())

print("\nUnique Sub Categories:")
print(df["sub_category"].unique())

print("\nUnique Plans:")
print(df["plan"].unique())

print("\nTop 10 Fund Houses:")
print(df["fund_house"].value_counts().head(10))