# Trigram Language Model

This project implements a trigram (N=3) statistical language model from scratch in Python. The model learns word transition probabilities from a text corpus and can generate new text using probabilistic sampling.

---

## 📁 Project Structure

```
trigram-assignment/
│
├── data/
│   └── example_corpus.txt
│
├── src/
│   ├── generate.py
│   ├── ngram_model.py
│   └── utils.py
│
└── evaluation.md
```

---

## ✅ Requirements

* Python 3.8+
* (Optional) Virtual environment

No ML libraries are required.

---

## 📦 Setup Instructions

### 1️⃣ Clone or Download

```
git clone <repo-url>
```

Or download and unzip.

### 2️⃣ Create a Virtual Environment (Optional)

```
python -m venv ven
```

Activate:

* Windows:

  ```
  ven\Scripts\activate
  ```
* macOS/Linux:

  ```
  source ven/bin/activate
  ```

### 3️⃣ Install Dependencies

If `requirements.txt` is present:

```
pip install -r requirements.txt
```

---

## 🧠 How It Works

* The model tokenizes text
* Adds start `<s>` and end `</s>` markers
* Builds trigram frequency counts
* Converts counts into probabilities
* Generates text by sampling the next word based on the probability distribution

---

## 🚀 Running the Model

### Basic Usage

From the project root:

```
python src/generate.py
```

This will:

* Train on `data/example_corpus.txt`
* Generate text with default length (50 tokens)

---

## ⚙ Command-Line Arguments

The script supports:

| Argument   | Description                                      | Example                  |
| ---------- | ------------------------------------------------ | ------------------------ |
| `--corpus` | Path to training text                            | `--corpus data/book.txt` |
| `--length` | Maximum generated tokens                         | `--length 150`           |
| `--seed`   | Optional random seed for reproducible generation | `--seed 42`              |

### Example Usage

#### 1️⃣ Generate with a different corpus

```
python src/generate.py --corpus data/alice.txt
```

#### 2️⃣ Generate longer text (150 tokens)

```
python src/generate.py --length 150
```

#### 3️⃣ Make output reproducible

```
python src/generate.py --length 150 --seed 42
```

#### 4️⃣ Combine everything

```
python src/generate.py --corpus data/alice.txt --length 200 --seed 10
```

---

## 📝 Editing the Training Text

Replace the corpus file:

```
data/example_corpus.txt
```

with any `.txt` file, ideally sourced from Project Gutenberg.

---

## 🔧 Troubleshooting

### Module import errors

❌ Running from inside `/src` may cause import problems.
✔ Always run from project root:

```
python src/generate.py
```

### File not found

Make sure the corpus path exists:

```
data/example_corpus.txt
```

---

## 📄 Evaluation

The design and implementation summary is documented in:

```
evaluation.md
```

---

## 📚 Credits

* Public text obtained from Project Gutenberg
* Fully implemented using standard Python and data structures

---

Happy text generation!
