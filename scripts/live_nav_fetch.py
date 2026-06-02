import requests
import pandas as pd
import os

os.makedirs("data/raw/live_nav", exist_ok=True)
funds = {
    "HDFC_TOP100":125497,
    "SBI_BLUECHIP":119551,
    "ICICI_BLUECHIP":120503,
    "NIPPON_LARGECAP":118632,
    "AXIS_BLUECHIP":119092,
    "KOTAK_BLUECHIP":120841
}
for fund_name, scheme_code in funds.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    file_path = f"data/raw/live_nav/{fund_name}.csv"

    nav_df.to_csv(file_path,index=False)

    print(f"Saved : {file_path}")

print("All NAV files downloaded successfully")