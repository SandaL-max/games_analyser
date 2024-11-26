import requests
import pandas as pd
import json
from tabulate import tabulate

url = "https://steamspy.com/api.php?request=all&page=0"
response = requests.get(url)
df = pd.DataFrame.from_dict(response.json()).transpose().drop("appid", axis=1)
with open("output.csv", "w") as file:
    file.write(df.to_csv(index_label="appid"))
df = pd.read_csv("output.csv", index_col="appid")
print(df.head())
