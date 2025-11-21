from data_preprocessing import load_and_clean
from ngram_model import TrigramModel

def main():
    text = load_and_clean("data/alice.txt")

    model = TrigramModel()
    model.fit(text)

    generated = model.generate(150)

    print("\nGenerated Text:\n")
    print(generated)

if __name__ == "__main__":
    main()
