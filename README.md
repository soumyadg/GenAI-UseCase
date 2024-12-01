---
![plot](./directory_1/directory_2/.../directory_n/49049.jpg)


# **GenAI Use Case Analysis**



This project leverages AI-powered techniques to analyze customer service transcripts. It identifies **sentiment** (positive, neutral, negative) and determines the **call outcome** (issue resolved, follow-up action needed). The solution is designed to help businesses improve customer interactions by providing actionable insights from conversations.

---

## **Features**
- **Sentiment Analysis**:
  - Uses a pre-trained RoBERTa model (`cardiffnlp/twitter-roberta-base-sentiment`) to classify transcript sentiment as positive, neutral, or negative.
- **Call Outcome Classification**:
  - Employs OpenAI GPT and Hugging Face zero-shot classification to categorize outcomes into "issue resolved" or "follow-up action needed."
- **Robust Testing**:
  - Includes test scripts and sample transcripts to validate the functionality.

---

## **Folder Structure**
```plaintext
project/
├── src/
│   ├── analyze_transcripts.py       # Main script to process transcripts
│   ├── call_outcome_analysis.py     # Classifies call outcomes
│   ├── sentiment_analysis.py        # Performs sentiment analysis
├── data/
│   ├── processed_transcripts/       # Contains input .txt transcript files
│   └── results.csv                  # Output file with analysis results
├── tests/
│   ├── test_script.py               # Test script for validating functionality
│   ├── test_transcripts.txt         # Sample transcripts for testing
├── requirements.txt                 # List of dependencies
├── README.md                        # Project documentation
```

---

## **Setup Instructions**

Follow these steps to set up the project and run the scripts:

### **1. Clone the Repository**
```bash
git clone <repository-url>
cd project
```

### **2. Create a Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # On Mac/Linux
env\Scripts\activate     # On Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Add Transcripts**
- Place `.txt` transcript files into the `data/processed_transcripts/` directory.
- Each file should contain one customer-agent interaction.

### **5. Run the Main Script**
Process all transcripts and generate the results:
```bash
python src/analyze_transcripts.py
```

### **6. View Results**
- The output will be saved as `results.csv` in the `data/` directory.
- The file contains the following columns:
  - `file_name`: Name of the processed transcript file.
  - `customer_text`: The content of the transcript.
  - `sentiment`: Sentiment classification (positive, neutral, or negative).
  - `determine_outcome`: Raw classification result.
  - `call_outcome`: Final classification (issue resolved or follow-up action needed).

---

## **Testing**

### **Test Transcripts**
Sample transcripts for testing are located in `tests/test_transcripts.txt`. These cover a variety of scenarios:
- Positive sentiment with resolved issues.
- Neutral sentiment requiring follow-up.
- Negative sentiment with unresolved issues.

### **Run Test Script**
Run the `tests/test_script.py` to validate the functionality of sentiment analysis and call outcome classification:
```bash
python tests/test_script.py
```

### **Sample Output**
For each transcript:
- Sentiment analysis results (e.g., positive, neutral, negative).
- Call outcome classification (e.g., issue resolved, follow-up action needed).

---

## **How It Works**

### **1. Sentiment Analysis**
- A pre-trained RoBERTa model (`cardiffnlp/twitter-roberta-base-sentiment`) analyzes the sentiment of the customer text.
- Results are mapped to `positive`, `neutral`, or `negative`.

### **2. Call Outcome Classification**
- OpenAI GPT identifies and categorizes call outcomes based on the conversation context.
- Hugging Face zero-shot classification ensures accurate predictions for new scenarios.

---

## **Dependencies**
The project requires the following Python libraries:
- `transformers`
- `torch`
- `numpy`
- `pandas`
- `tqdm`
- `openai`

Install them via:
```bash
pip install -r requirements.txt
```

---

## **Example Transcripts**

### **Input**
Sample customer-agent transcript:
```plaintext
Customer: Hi, I can’t log in to my account.
Agent: Let me reset your password. Can I confirm your email?
Customer: Yes, it’s john.doe@example.com.
Agent: I’ve sent you a password reset email. Please check your inbox.
Customer: Thank you for your help!
```

### **Output**
```csv
file_name,customer_text,sentiment,determine_outcome,call_outcome
transcript_1.txt,"Hi, I can’t log in to my account...",positive,"Issue resolved","issue resolved"
```

---

## **Future Enhancements**
- Add multilingual support for transcripts.
- Incorporate advanced metrics for sentiment intensity.
- Develop a web-based dashboard for real-time analysis.

---

## **Contact**
For questions or feedback, reach out to:
- **Name**: [Your Name]
- **Email**: [Your Email]
- **GitHub**: [GitHub Profile URL]
