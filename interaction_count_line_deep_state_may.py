mport pandas as pd
import matplotlib.pyplot as plt

CountDf=pd.read_pickle("2022-07_tweet_data_deep_state.pkl")
x= CountDf["tweet_id"]
y= CountDf["interact_count"]

plt.plot(x,y)

plt.gca().axes.get_xaxis().set_visible(False)

plt.show()
