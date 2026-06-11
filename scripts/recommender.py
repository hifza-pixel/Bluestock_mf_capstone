"""
Mutual Fund Recommendation System

This script recommends the top 3 mutual funds
based on investor risk appetite and Sharpe Ratio.
Author: Hifza Tanveer
Project: Bluestock Mutual Fund Capstone
"""
import pandas as pd

performance = pd.read_csv(
    "data/processed/scheme_performance_cleaned.csv"
)

def recommend_funds(risk_level):

    result = (
        performance[
            performance['risk_grade'] == risk_level
        ]
        .sort_values(
            'sharpe_ratio',
            ascending=False
        )
        .head(3)
    )

    return result[
        [
            'amfi_code',
            'scheme_name',
            'risk_grade',
            'sharpe_ratio'
        ]
    ]

risk = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

print(
    recommend_funds(risk)
)