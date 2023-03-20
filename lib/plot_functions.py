import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    from wordcloud import WordCloud
except ImportError:
    print("WordCloud not installed. Please install WordCloud to use this feature.")
    print("pip install wordcloud")

try:
    from textblob import TextBlob
except ImportError:
    print("TextBlob not installed. Please install TextBlob to use this feature.")
    print("pip install textblob")

def line_chart(dataset, x_data, y_data, hide_x=False):
    """ Plot a line chart of the given dataset. """
    df=pd.read_pickle(dataset)
    x= df[x_data]
    y= df[y_data]

    # Horizontal Bar Plot
    plt.plot(x,y)
    plt.gca().axes.get_xaxis().set_visible(hide_x)

    # Label Axes
    x_label = x_data.replace("_", " ").title()
    y_label = y_data.replace("_", " ").title()
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Show Plot
    plt.show()


def bar_chart(dataset, x_data, y_data, hide_x=False):
    """ Plot a bar chart of the given dataset. """
    df = pd.read_pickle(dataset)
    x = df[x_data]
    y = df[y_data]

    # Horizontal Bar Plot
    plt.bar(x, y)
    plt.gca().axes.get_xaxis().set_visible(hide_x)

    # Label Axes
    x_label = x_data.replace("_", " ").title()
    y_label = y_data.replace("_", " ").title()
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Show Plot
    plt.show()


def pie_chart(*datasets):
    """ Plot a pie chart of the given dataset. """
    # Intialize empty array
    y = np.empty(len(datasets))

    # Load data into array
    for i, dataset in enumerate(datasets):
        df = pd.read_pickle(dataset)
        y[i] = df.size

    # Plot pie chart
    plt.pie(y)
    plt.show()


def word_cloud(dataset, data_key, filters=None):
    """ Plot a word cloud of the given dataset. """
    df = pd.read_pickle(dataset)
    text = df[data_key].to_string()

    # Remove words starting with filter
    if filters:
        for f in filters:
            text = " ".join([word for word in text.split() if not word.startswith(f)])

    wordcloud = WordCloud().generate(text)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


def get_sentiment(text):
    """ Get the sentiment of the given dataset. """
    blob = TextBlob(text)
    return blob.sentiment.polarity

def sentiment_analysis(dataset, data_key):
    """ Plot a sentiment analysis of the given dataset. """
    df = pd.read_pickle(dataset)

    df['sentiment'] = df[data_key].apply(get_sentiment)

    # Create a histogram of the sentiment values
    plt.hist(df['sentiment'], bins=20)

    # Label the axes
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Tweets')

    # Show the plot
    plt.title('Sentiment Analysis of Tweets')
    plt.show()

