# sentiment_analysis.py

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon (run once)
nltk.download('vader_lexicon')

def sentiment_analysis(text):
    """
    Analyze the sentiment of a given text using NLTK's VADER SentimentIntensityAnalyzer.

    Parameters:
        text (str): The text to analyze.

    Returns:
        dict: Sentiment scores with keys:
              'neg' (negative), 'neu' (neutral), 'pos' (positive), 'compound' (overall sentiment).
    """
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    return sentiment

if __name__ == '__main__':
    # Example usage
    sample_text = "This is a sample text with positive sentiment."
    scores = sentiment_analysis(sample_text)

    print("Text:", sample_text)
    print("Sentiment Scores:", scores)
