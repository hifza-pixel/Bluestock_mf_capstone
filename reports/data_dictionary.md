# Data Dictionary

## fund_master

| Column            | Data Type | Description              |
| ----------------- | --------- | ------------------------ |
| amfi_code         | Integer   | Unique AMFI Scheme Code  |
| fund_house        | Text      | Mutual Fund Company Name |
| scheme_name       | Text      | Mutual Fund Scheme Name  |
| category          | Text      | Fund Category            |
| sub_category      | Text      | Fund Sub Category        |
| plan              | Text      | Direct/Regular Plan      |
| launch_date       | Date      | Scheme Launch Date       |
| benchmark         | Text      | Benchmark Index          |
| expense_ratio_pct | Float     | Expense Ratio Percentage |
| exit_load_pct     | Float     | Exit Load Percentage     |

## nav_history

| Column    | Data Type | Description     |
| --------- | --------- | --------------- |
| amfi_code | Integer   | Scheme Code     |
| date      | Date      | NAV Date        |
| nav       | Float     | Net Asset Value |

## investor_transactions

| Column           | Data Type | Description             |
| ---------------- | --------- | ----------------------- |
| investor_id      | Integer   | Investor Identifier     |
| transaction_date | Date      | Transaction Date        |
| transaction_type | Text      | SIP/Lumpsum/Redemption  |
| amount_inr       | Float     | Transaction Amount      |
| state            | Text      | Investor State          |
| city             | Text      | Investor City           |
| kyc_status       | Text      | KYC Verification Status |

## scheme_performance

| Column            | Data Type | Description         |
| ----------------- | --------- | ------------------- |
| return_1yr_pct    | Float     | 1 Year Return       |
| return_3yr_pct    | Float     | 3 Year Return       |
| return_5yr_pct    | Float     | 5 Year Return       |
| alpha             | Float     | Alpha Value         |
| beta              | Float     | Beta Value          |
| sharpe_ratio      | Float     | Sharpe Ratio        |
| expense_ratio_pct | Float     | Expense Ratio       |
| risk_grade        | Text      | Risk Classification |
