# import sys
# import os

# # Add the `src` directory to Python's module search path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# from sentiment_analysis import analyze_sentiment
# from call_outcome_analysis import classify_call_outcome
# import pandas as pd


# from src.sentiment_analysis import analyze_sentiment
# from src.call_outcome_analysis import classify_call_outcome
# import pandas as pd
# import os

# # Debugging: Print current working directory
# print(f"Current working directory: {os.getcwd()}")


# from src.call_outcome_analysis import classify_call_outcome
# from test_script import load_test_transcripts  

# def test_call_outcome():
#     """Test the call outcome classification logic."""
#     # Load test transcripts
#     transcripts = load_test_transcripts("tests/test_transcripts.txt")
    
#     # Create a DataFrame with necessary columns
#     df = pd.DataFrame({
#         "file_name": [f"test_file_{i}.txt" for i in range(len(transcripts))],  # Placeholder file names
#         "customer_text": transcripts
#     })
    
#     # Print DataFrame before classification (for debugging)
#     print("Input DataFrame:")
#     print(df.head())
    
#     # Classify call outcomes
#     results = classify_call_outcome(df)
    
#     # Print the results
#     print("Results DataFrame:")
#     print(results)




# # Function to load test transcripts from a file
# def load_test_transcripts(file_path):
#     print(f"Attempting to load test transcripts from: {file_path}")
#     with open(file_path, "r") as file:
#         return [line.strip() for line in file.read().split("###") if line.strip()]

# # Test Sentiment Analysis
# def test_sentiment_analysis():
#     transcripts = load_test_transcripts("tests/test_transcripts.txt")
#     print("Testing Sentiment Analysis...")
#     for transcript in transcripts:
#         sentiment = analyze_sentiment(transcript)
#         print(f"Transcript: {transcript[:50]}... -> Sentiment: {sentiment}")

# # Test Call Outcome Analysis
# def test_call_outcome():
#     transcripts = load_test_transcripts("tests/test_transcripts.txt")
#     df = pd.DataFrame({"customer_text": transcripts})
#     print("Testing Call Outcome Analysis...")
#     results = classify_call_outcome(df)
#     print(results)

# if __name__ == "__main__":
#     print("Starting Tests...")
#     test_sentiment_analysis()
#     test_call_outcome()


import sys
import os
import pandas as pd

# Add the `src` directory to Python's module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import functions from src and test_utils
from src.sentiment_analysis import analyze_sentiment
from src.call_outcome_analysis import classify_call_outcome
from test_utils import load_test_transcripts  # Import from test_utils.py

# Debugging: Print current working directory
print(f"Current working directory: {os.getcwd()}")

def test_sentiment_analysis():
    """Test the sentiment analysis logic."""
    transcripts = load_test_transcripts("tests/test_transcripts.txt")
    print("Testing Sentiment Analysis...")
    for transcript in transcripts:
        sentiment = analyze_sentiment(transcript)
        print(f"Transcript: {transcript[:50]}... -> Sentiment: {sentiment}")

def test_call_outcome():
    """Test the call outcome classification logic."""
    transcripts = load_test_transcripts("tests/test_transcripts.txt")
    df = pd.DataFrame({
        "file_name": [f"test_file_{i}.txt" for i in range(len(transcripts))],  # Placeholder file names
        "customer_text": transcripts
    })

    # Print DataFrame before classification (for debugging)
    print("Input DataFrame:")
    print(df.head())

    # Classify call outcomes
    results = classify_call_outcome(df)

    # Print the results
    print("Results DataFrame:")
    print(results)

if __name__ == "__main__":
    print("Starting Tests...")
    test_sentiment_analysis()
    test_call_outcome()
