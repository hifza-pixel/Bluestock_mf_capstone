import pandas as pd

files = [
    "08_investor_transactions.csv",
    "07_scheme_performance.csv",
    "03_aum_by_fund_house.csv"
]

for file in files:
    print("\n", "="*50)
    print(file)
    print("="*50)

    df = pd.read_csv(f"data/raw/{file}")
    print(df.columns.tolist())