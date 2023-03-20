import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dfd = pd.read_pickle("data/2022-05_tweet_data_deep_state.pkl")
dfc = pd.read_pickle("data/2022-05_tweet_data_combined.pkl")
dfa = pd.read_pickle("data/2022-05_tweet_data_anti_vax.pkl")

y = np.array([dfc.size,dfd.size-dfc.size])

plt.pie(y)
plt.show()
