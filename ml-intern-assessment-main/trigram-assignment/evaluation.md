# Evaluation

Please provide a 1-page summary of your design choices for the Trigram Language Model.

This should include:

- How you chose to store the n-gram counts.
- How you handled text cleaning, padding, and unknown words.
- How you implemented the `generate` function and the probabilistic sampling.
- Any other design decisions you made and why you made them.


## Overview

This project implements a trigram (N=3) statistical language model from scratch using pure Python. The model learns word continuation probabilities from a text corpus and generates new text by probabilistic sampling. The objective is to demonstrate understanding of probabilistic modeling, counting structures, tokenization, and text generation without using machine-learning libraries.

## Data Extraction & Cleaning

The training text was sourced from Project Gutenberg (“Alice in Wonderland”). The preprocessing pipeline included:

* Converting all text to lowercase for consistency.
* Removing punctuation and non-alphabetic characters.
* Normalizing multiple whitespace characters.
* Splitting text into sentences.
* Padding each sentence with start and end tokens (`<s>` and `</s>`).
* Replacing rare or unseen tokens with an `<unk>` placeholder to handle unknown words.

This step standardizes input and ensures the model has well-formed sequences to learn from.

## N-Gram Representation

Trigrams were represented using nested dictionaries with `Counter` objects:
counts[(w1, w2)][w3] → frequency of the trigram

Additionally, a separate structure tracked total occurrences of each `(w1, w2)` context:
context_totals[(w1, w2)] → total number of trigram continuation

This allows easy computation of conditional probabilities:
P(w3 | w1, w2) = counts[(w1, w2)][w3] / context_totals[(w1, w2)]

This approach is efficient, readable, and avoids unnecessary complexity.

## Text Generation Strategy

Generation begins with `["<s>", "<s>"]`. The model repeatedly:

1. Looks up possible next words for the context `(w1, w2)`
2. Computes continuation probabilities from trigram counts
3. Samples the next word using `random.choices` based on probability weights
4. Updates the context and continues until `</s>` or a maximum length is reached

This probabilistic sampling ensures diverse sentence outputs rather than deterministic repetition.

## Design Rationale

* **Plain Python and dictionaries** make the implementation transparent and educational.
* **Counters and tuple keys** minimize overhead and match the mathematical representation of n-grams.
* **Sampling instead of greedy selection** allows creative text generation while remaining grounded in statistical likelihood.
* **Padding tokens** make sentence boundaries explicit and improve grammatical structure in generated text.

## Limitations & Future Work

* **Unseen sequences have zero probability** (no smoothing). Implementing Laplace, Good-Turing, or Katz backoff would improve robustness.
* **Small training datasets yield repetitive output.** Larger corpora produce more realistic language.
* **No support for dynamic vocabulary expansion** during generation.

Despite these limitations, the implementation demonstrates a complete and functional trigram language model constructed from first principles.
