# Information Retrieval Assignment: Tokenization Evaluation and Character Normalization

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![NLTK](https://img.shields.io/badge/NLTK-3.8%2B-green.svg)](https://www.nltk.org/)
[![spaCy](https://img.shields.io/badge/spaCy-3.5%2B-orange.svg)](https://spacy.io/)

This repository contains the implementation, datasets, evaluation outputs, and final report for an **Information Retrieval preprocessing assignment** based on the Tesla Twitter/X corpus (`Tesla.csv`). The work is divided into two tasks: evaluation of tokenization methods for informal social-media text, and normalization of repeated characters while preserving structured entities.

**Final Report:** [IR_Assignment_Final_Report.pdf](IR_Assignment_Final_Report.pdf)

---

## Assignment Overview

### Task 1: Tokenization Performance Evaluation

Task 1 compares three tokenizers on a **50-post feature-rich evaluation subset** selected from the Tesla corpus:

- NLTK `TweetTokenizer`
- spaCy (`en_core_web_sm`)
- NLTK `word_tokenize`

The evaluation measures whether hashtags, mentions, URLs, and emojis are preserved as complete tokens. It also records the total number of tokens and the average number of tokens generated per post.

#### Task 1 Results

| Tokenizer | Hashtag (%) | Mention (%) | URL (%) | Emoji (%) | Total Tokens | Avg. / Post |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| **NLTK TweetTokenizer** | **100.00** | **100.00** | **100.00** | **95.35** | 1,814 | 36.28 |
| spaCy (`en_core_web_sm`) | 0.00 | 97.78 | 100.00 | **95.35** | 2,013 | 40.26 |
| NLTK `word_tokenize` | 0.00 | 0.00 | 0.00 | 34.88 | **2,151** | **43.02** |

For the social-media structures evaluated in this assignment, `TweetTokenizer` gives the strongest overall preservation. The larger token count produced by `word_tokenize` mainly reflects additional fragmentation of social-media-specific elements.

### Task 2: Repeated Character Normalization

Task 2 uses a separate set of **100 posts**, excluding the posts selected for Task 1. It detects alphabetic character repetitions of three or more consecutive occurrences using:

```text
([A-Za-z])\1{2,}
```

The normalization pipeline:

1. protects URLs, hashtags, mentions, and cashtags;
2. detects repeated-character sequences in the remaining text;
3. generates one-character and two-character reduction candidates;
4. selects the more plausible lexical form using Zipf frequency scores from `wordfreq`;
5. restores the original casing and protected entities.

This allows forms such as `noooooothing` to be normalized while leaving structured entities such as `@mentions`, `#hashtags`, URLs, and `$cashtags` unchanged.

---

## Repository Structure

```text
.
├── CODE/
│   ├── data/
│   │   ├── Tesla.csv
│   │   ├── task1_posts.csv
│   │   ├── task1_ground_truth.csv
│   │   ├── task2_posts.csv
│   │   └── task2_normalized.csv
│   ├── results/
│   │   ├── evaluation_summary.csv
│   │   ├── tokenizer_results.csv
│   │   ├── tokenizer_output.txt
│   │   ├── error_analysis.txt
│   │   └── task2_repeated_patterns.txt
│   ├── src/
│   │   ├── check_dataset.py
│   │   ├── select_ds.py
│   │   ├── ground_truth.py
│   │   ├── tokenization.py
│   │   ├── evaluation.py
│   │   ├── error_analysis.py
│   │   ├── task2_post.py
│   │   ├── task2_inspect.py
│   │   ├── task2_normalize.py
│   │   └── task2_compare.py
│   └── requirements.txt
├── IR_Assignment_Final_Report.pdf
├── Task_1_Tokenization_Performance_Report.pdf
├── Task_2_Repeated_Character_Normalization_Report.pdf
└── README.md
```

---

## Environment Setup

From the repository root:

```bash
cd CODE
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m spacy download en_core_web_sm
python3 -m nltk.downloader punkt punkt_tab
```

On Windows, activate the virtual environment with:

```powershell
.venv\Scripts\activate
```

---

## Reproducing Task 1

Run the scripts in the following order:

```bash
cd CODE
python3 src/select_ds.py
python3 src/ground_truth.py
python3 src/tokenization.py
python3 src/evaluation.py
python3 src/error_analysis.py
```

The main outputs are written to:

- `data/task1_posts.csv`
- `data/task1_ground_truth.csv`
- `results/tokenizer_results.csv`
- `results/evaluation_summary.csv`
- `results/error_analysis.txt`

---

## Reproducing Task 2

Run:

```bash
cd CODE
python3 src/task2_post.py
python3 src/task2_inspect.py
python3 src/task2_normalize.py
python3 src/task2_compare.py
```

The main outputs are written to:

- `data/task2_posts.csv`
- `data/task2_normalized.csv`
- `results/task2_repeated_patterns.txt`

---

## Methodological Notes

- Task 1 and Task 2 use disjoint subsets of the source corpus.
- Ground-truth hashtags, mentions, and URLs are extracted from the raw text before tokenization; emojis are identified using the Python `emoji` package.
- A feature is counted as preserved only when the complete ground-truth string appears as a single tokenizer output token.
- Task 2 protects structured social-media entities before repeated-character normalization and restores them afterward.
- The generated CSV and text files in `CODE/results/` provide the empirical outputs used for the reported findings.

---

## Reports

- [Final Assignment Report](IR_Assignment_Final_Report.pdf)
- [Task 1: Tokenization Performance Report](Task_1_Tokenization_Performance_Report.pdf)
- [Task 2: Repeated Character Normalization Report](Task_2_Repeated_Character_Normalization_Report.pdf)

---

## AI Usage Statement

AI-assisted tools were used for coding support, regular-expression refinement, methodology guidance, debugging, and report structuring. Dataset selection, script execution, tokenizer outputs, normalization outputs, quantitative measurements, and error analysis were produced and verified by running the project code locally.
