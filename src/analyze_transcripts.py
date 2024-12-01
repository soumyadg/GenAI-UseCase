import os
import pandas as pd
from tqdm import tqdm
from sentiment_analysis import analyze_sentiment
from call_outcome_analysis import classify_call_outcome

transcripts_dir = os.path.join(os.path.dirname(__file__), '../data/processed_transcripts/')
results_path = os.path.join(os.path.dirname(__file__), '../data/results.csv')

def process_transcripts(transcripts_dir, results_path):
    """Process all transcripts to analyze sentiment and classify call outcomes."""
    if not os.path.exists(transcripts_dir):
        os.makedirs(transcripts_dir)
        print(f"Created missing directory: {transcripts_dir}")
        return

    # Collect transcripts into a DataFrame
    data = []
    for transcript_file in os.listdir(transcripts_dir):
        file_path = os.path.join(transcripts_dir, transcript_file)
        if os.path.isfile(file_path) and file_path.endswith('.txt'):
            with open(file_path, 'r') as file:
                transcript = file.read()
                data.append({"file_name": transcript_file, "customer_text": transcript})

    df = pd.DataFrame(data)

    # Enable tqdm progress bar
    tqdm.pandas()

    # Analyze sentiment for each transcript
    print("Analyzing sentiment...")
    df['sentiment'] = df['customer_text'].progress_apply(analyze_sentiment)

    # Classify call outcomes
    print("Classifying call outcomes...")
    classified_df = classify_call_outcome(df)

    # Merge sentiment results with call outcome results
    classified_df['sentiment'] = df['sentiment']

    # Save results to CSV
    classified_df.to_csv(results_path, index=False)
    print(f"Results saved to {results_path}")

if __name__ == "__main__":
    process_transcripts(transcripts_dir, results_path)
