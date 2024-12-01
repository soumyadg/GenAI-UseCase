from openai import OpenAI
import pandas as pd
from tqdm import tqdm
from transformers import pipeline

# Initialize the OpenAI client
client = OpenAI(
    api_key="Open_AI Key Here"
)

# Zero-shot classification model
zero_shot_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def determine_outcome(text):
    """
    Determines the call outcome as either 'issue resolved' or 'follow-up action needed'.
    """
    try:
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant that determines the outcome of customer service calls."
            },
            {
                "role": "user",
                "content": f"Based on the following conversation, determine if the issue is resolved or if follow-up action is needed:\n{text}"
            }
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0
        )
        response_message = response.choices[0].message.content.strip()
        return response_message
    except Exception as e:
        print(f"Error in outcome determination: {e}")
        return "Error"

def classify_call_outcome(df):
    """
    Classifies call outcomes using OpenAI GPT and zero-shot classification.
    """
    # Enable progress bar for pandas
    tqdm.pandas()

    # Ensure no null values in 'customer_text'
    df['customer_text'] = df['customer_text'].fillna('')

    # Determine outcome using OpenAI GPT
    df['determine_outcome'] = [
        determine_outcome(text) for text in tqdm(df['customer_text'], desc="Determining Outcome")
    ]

    # Define possible outcomes for zero-shot classification
    labels = ["issue resolved", "follow-up action needed"]

    # Apply zero-shot classification
    df['call_outcome'] = df['determine_outcome'].progress_apply(
        lambda x: zero_shot_classifier(x, candidate_labels=labels)['labels'][0]
    )

    return df[['file_name', 'customer_text', 'determine_outcome', 'call_outcome']]
