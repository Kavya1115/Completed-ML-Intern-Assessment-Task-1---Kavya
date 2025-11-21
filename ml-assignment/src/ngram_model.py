import random
from collections import defaultdict

class TrigramModel:
    def __init__(self):
        self.counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        self.context_totals = defaultdict(lambda: defaultdict(int))
        self.vocab = set()

    def tokenize(self, text):
        words = text.split()
        return words

    def fit(self, text):
        words = ["<s>", "<s>"] + self.tokenize(text) + ["</s>"]

        for w1, w2, w3 in zip(words, words[1:], words[2:]):
            self.counts[w1][w2][w3] += 1
            self.context_totals[w1][w2] += 1
            self.vocab.update([w1, w2, w3])

    def generate(self, max_words=50):
        w1, w2 = "<s>", "<s>"
        output = []

        for _ in range(max_words):
            next_words = list(self.counts[w1][w2].keys())
            counts = list(self.counts[w1][w2].values())

            if not next_words:
                break
            next_word = random.choices(next_words, weights=counts, k=1)[0]

            if next_word == "</s>":
                break
            output.append(next_word)
            w1, w2 = w2, next_word

        return " ".join(output)
