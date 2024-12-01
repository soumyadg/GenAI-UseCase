
import pytest
from sentiment_analysis import analyze_sentiment

def test_analyze_sentiment():
    assert analyze_sentiment("I am happy with the service.") == "positive"
    assert analyze_sentiment("I am very disappointed.") == "negative"
    assert analyze_sentiment("It's okay.") == "neutral"
