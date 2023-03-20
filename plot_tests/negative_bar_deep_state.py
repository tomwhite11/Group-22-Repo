import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_pickle("data/2022-07_tweet_data_deep_state.pkl")
x = df['tweet_id']
y = df['negative_tweet_sentiment']

# Horizontal Bar Plot
plt.bar(x, y)

plt.gca().axes.get_xaxis().set_visible(False)
# Show Plot
plt.show()
