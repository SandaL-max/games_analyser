from time import sleep
import progressbar

bar = progressbar.ProgressBar(
    maxval=60.0,
    widgets=[
        "Progress of downloading dataset: ",  # Статический текст
        progressbar.Bar(left="[", marker="=", right="]"),  # Прогресс
        progressbar.SimpleProgress(),  # Надпись "6 из 10"
    ],
).start()

for i in range(80):
    bar.update(i)
bar.finish()
