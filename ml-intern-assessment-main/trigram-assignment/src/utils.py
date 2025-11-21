# This file is optional.
# You can add any utility functions you need for your implementation here.
import re

def tokenize(text):
    text = text.lower()
    return re.findall(r"\b\w+\b", text)

