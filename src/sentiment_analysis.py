from transformers import pipeline

# Initialize the RoBERTa-based sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

# Mapping dictionary for sentiment labels
sentiment_mapping = {
    "LABEL_0": "negative",
    "LABEL_1": "neutral",
    "LABEL_2": "positive"
}

def analyze_sentiment(transcript):
    """Analyze the sentiment of a given transcript."""
    try:
        max_length = 512
        truncated_transcript = transcript[:max_length]

        # Use the pre-trained model to analyze sentiment
        sentiment_result = sentiment_analyzer(truncated_transcript)[0]['label']
        # Map the result to positive, negative, or neutral
        return sentiment_mapping.get(sentiment_result, "neutral")
    except Exception as e:
        print(f"Error in sentiment analysis for transcript: {transcript[:100]}...")  # First 100 characters
        print(f"Exception: {e}")
        return "neutral"