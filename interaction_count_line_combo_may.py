#errors in picking uip interactions
import pandas as pd
import matplotlib.pyplot as plt

CountDf=pd.read_pickle("2022-05_tweet_data_combined.pkl")
x= CountDf["tweet_id"]
y= CountDf["interact_count"]

plt.plot(x,y)

plt.gca().axes.get_xaxis().set_visible(False)

plt.show()
