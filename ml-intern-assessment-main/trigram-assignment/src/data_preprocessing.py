import re

def load_and_clean(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().lower()

    # Remove non-alphabetic characters except spaces
    text = re.sub(r'[^a-z\s]', '', text)

    # Collapse multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text

