# Bluestock Mutual Fund Analytics Capstone

## Project Overview

This project analyzes the Indian Mutual Fund industry using data analytics, SQL, Python, Machine Learning concepts, and Power BI. The objective is to perform end-to-end data analysis, generate investment insights, evaluate fund performance, and build an interactive dashboard for decision-making.

---

## Objectives

* Clean and validate mutual fund datasets
* Design and load a SQLite database
* Perform Exploratory Data Analysis (EDA)
* Analyze fund performance using financial metrics
* Build interactive Power BI dashboards
* Perform advanced investor and risk analytics
* Generate actionable investment insights

---

## Dataset Description

The project uses the following datasets:

* fund_master.csv
* nav_history.csv
* aum_by_fund_house.csv
* monthly_sip_inflows.csv
* category_inflows.csv
* industry_folio_count.csv
* scheme_performance.csv
* investor_transactions.csv
* portfolio_holdings.csv
* benchmark_indices.csv

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SQLite
* SQLAlchemy
* Power BI
* Jupyter Notebook
* Git & GitHub

---

## Project Structure

```text
bluestock_mf_capstone/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── scripts/
│   ├── recommender.py
│   └── run_pipeline.py
│
├── reports/
│   ├── Dashboard.pdf
│   ├── rolling_sharpe_chart.png
│   ├── var_cvar_report.csv
│   └── dashboard screenshots
│
├── bluestock_mf.db
├── bluestock_mf_dashboard.pbix
└── README.md
```

## ETL Process

### Extract

Load raw CSV datasets.

### Transform

* Data cleaning
* Missing value handling
* Date conversion
* Validation checks
* Standardization

### Load

Load cleaned datasets into SQLite database using SQLAlchemy.

---

## How to Run

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn plotly sqlalchemy scipy
```

### Run Pipeline

```bash
python scripts/run_pipeline.py
```

### Run Recommender

```bash
python scripts/recommender.py
```

---

## Dashboard

Open:

```text
bluestock_mf_dashboard.pbix
```

using Microsoft Power BI Desktop.

---

## Key Analyses Performed

### EDA

* NAV trend analysis
* SIP inflow analysis
* Category inflow heatmap
* Investor demographics
* Geographic analysis

### Performance Analytics

* CAGR
* Sharpe Ratio
* Sortino Ratio
* Alpha & Beta
* Maximum Drawdown
* Fund Scorecard

### Advanced Analytics

* VaR & CVaR
* Rolling Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Fund Recommendation System
* HHI Concentration Analysis

---

## Deliverables

* Final_Report.pdf
* Bluestock_MF_Presentation.pptx
* bluestock_mf_dashboard.pbix
* Dashboard.pdf
* Advanced_Analytics.ipynb
* Performance_Analytics.ipynb
* EDA_Analysis.ipynb
* var_cvar_report.csv
* recommender.py

---

## Author

Hifza Tanveer

BCA Final Year Student

Bluestock Mutual Fund Analytics Capstone Project
