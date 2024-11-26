import requests
import pandas as pd
import json
from tabulate import tabulate
from time import sleep
import progressbar

bar = progressbar.ProgressBar(
    maxval=200.0,
    widgets=[
        "Progress of downloading dataset: ",  # Статический текст
        progressbar.Bar(left="[", marker="=", right="]"),  # Прогресс
        progressbar.SimpleProgress(),  # Надпись "6 из 10"
    ],
).start()

i = 60
while (
    response := requests.get(f"https://steamspy.com/api.php?request=all&page={i}")
).status_code == 200:
    df = pd.DataFrame.from_dict(response.json()).transpose().drop("appid", axis=1)
    df.to_csv(f"data/steamspy_dataset/page{i}.csv", index_label="appid")
    i += 1
    bar.update(i)
    sleep(70)

bar.finish()
print(i)
