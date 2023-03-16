import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_pickle("2022-05_tweet_data_combined.pkl")
x = df['tweet_id']
y = df['negative_tweet_sentiment']

# Horizontal Bar Plot
plt.bar(x, y)

plt.gca().axes.get_xaxis().set_visible(False)
# Show Plot
plt.show()
