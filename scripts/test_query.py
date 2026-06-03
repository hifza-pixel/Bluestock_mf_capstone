import sqlite3
import pandas as pd

conn = sqlite3.connect("data/db/bluestock_mf.db")

query = """
SELECT fund_house, aum_crore
FROM aum_by_fund_house
ORDER BY aum_crore DESC
LIMIT 5
"""

df = pd.read_sql_query(query, conn)

print(df)

conn.close()