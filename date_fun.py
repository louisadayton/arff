import datetime
import pandas as pd

df = pd.read_table("date.txt")
#print(pd.to_datetime(df["date"]))
for value in df["date"]:
    v = pd.to_datetime(value, errors = 'ignore').value.strftime("%Y-%m-%d")
    print(v)
    if isinstance(v, datetime.date):
        print("Holla!")

