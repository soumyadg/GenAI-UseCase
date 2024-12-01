def load_test_transcripts(file_path):
    """Load test transcripts from a file."""
    print(f"Loading test transcripts from: {file_path}")
    with open(file_path, "r") as file:
        return [line.strip() for line in file.read().split("###") if line.strip()]
