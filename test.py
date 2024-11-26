import requests
import pandas as pd
import json
from tabulate import tabulate

""" url = "https://steamspy.com/api.php?request=all&page=0"
response = requests.get(url)
df = pd.DataFrame.from_dict(response.json()).transpose().drop("appid", axis=1)
with open("output.csv", "w") as file:
    file.write(df.to_csv(index_label="appid")) """
# df = pd.read_csv("output.csv", index_col="appid")
# print(df.head())
df = None
with open("api.steampowered.com.json", "r") as file:
    df = pd.DataFrame(json.load(file)["applist"]["apps"]).set_index("appid").drop_duplicates().sort_index()
with open("output2.csv", "w") as file:
    file.write(df.to_csv(index_label="appid"))
print(df)

