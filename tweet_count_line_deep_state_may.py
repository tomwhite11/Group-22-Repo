import pandas as pd
import matplotlib.pyplot as plt

CountDf=pd.read_pickle("2022-05_tweet_count_deep_state.pkl")
x= CountDf["date"]
y= CountDf["count"]

plt.plot(x,y)

plt.gca().axes.get_xaxis().set_visible(False)

plt.show()
