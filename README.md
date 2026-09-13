# Information Retrieval Assignment: Twitter Tokenization & Character Normalization

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![NLTK](https://img.shields.io/badge/NLTK-3.8%2B-green.svg)](https://www.nltk.org/)
[![spaCy](https://img.shields.io/badge/spaCy-3.5%2B-orange.svg)](https://spacy.io/)

This repository contains the complete implementation, ground-truth dataset, automated test scripts, and comprehensive report for the **Information Retrieval (IR) Preprocessing Assignment** based on the Tesla Twitter Corpus (`Tesla.csv`).

📄 **Full Unified Assignment Report**: [IR_Assignment_Final_Report.md](IR_Assignment_Final_Report.md)

---

## 📌 Tasks Covered

### **Task 1: Tokenization Performance Evaluation**
Evaluates how three different tokenizers (`NLTK TweetTokenizer`, `spaCy`, `NLTK Word Tokenize`) handle microblog-native entities across **50 sampled tweets**:
- **Hashtag Preservation Rate (%)**
- **Mention Preservation Rate (%)**
- **URL Preservation Rate (%)**
- **Emoji Preservation Rate (%)**
- **Token Efficiency (Total Tokens & Avg Tokens/Post)**

#### **Task 1 Benchmark Results**
| Tokenizer | Hashtag (%) | Mention (%) | URL (%) | Emoji (%) | Total Tokens | Avg / Post |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **NLTK TweetTokenizer** | **100.0%** | **100.0%** | **100.0%** | **95.35%** | **1,814** | **36.28** |
| **spaCy (`en_core_web_sm`)** | 0.0% | 97.78% | 100.0% | 95.35% | 2,013 | 40.26 |
| **NLTK Word Tokenize** | 0.0% | 0.0% | 0.0% | 34.88% | 2,151 | 43.02 |

---

### **Task 2: Repeated Character Normalization**
A text normalization pipeline designed to eliminate character elongation (e.g., *sooo*, *yasss*) without damaging entity semantics:
- **Protection Masking**: Shields URLs, `#hashtags`, `@mentions`, and `$cashtags` (e.g. `$QQQ`, `$TSLA`) from modification.
- **Candidate Scoring**: Evaluates candidate forms using Zipf word frequency scoring via `wordfreq`.
- **Casing Preservation**: Maintains original UPPERCASE / Capitalization rules.

---

## 📁 Repository Structure

```
.
├── CODE/
│   ├── data/                   # Original dataset & generated task CSVs
│   │   ├── Tesla.csv           # Raw source tweet dataset
│   │   ├── task1_posts.csv     # 50 selected tweets for Task 1
│   │   ├── task1_ground_truth.csv # Ground truth labels
│   │   ├── task2_posts.csv     # 100 sampled tweets for Task 2
│   │   └── task2_normalized.csv # Output normalized tweets
│   ├── results/                # Evaluation logs and summary outputs
│   │   ├── evaluation_summary.csv
│   │   ├── error_analysis.txt
│   │   ├── tokenizer_output.txt
│   │   └── task2_repeated_patterns.txt
│   ├── src/                    # Python source code
│   │   ├── select_ds.py        # Task 1 sample selection algorithm
│   │   ├── ground_truth.py     # Ground truth extraction
│   │   ├── tokenization.py     # Tokenization pipeline runner
│   │   ├── evaluation.py       # Task 1 metrics calculator
│   │   ├── error_analysis.py   # Detailed error log generator
│   │   ├── task2_post.py       # Task 2 tweet selection
│   │   ├── task2_inspect.py    # Elongated pattern inspector
│   │   ├── task2_normalize.py  # Character normalization pipeline
│   │   └── task2_compare.py    # Before/After comparison script
│   └── requirements.txt        # Python package dependencies
├── IR_Assignment_Final_Report.md # Complete unified assignment report
├── Task_1_Tokenization_Performance_Report.pdf # Task 1 PDF report
├── Task_2_Repeated_Character_Normalization_Report.pdf # Task 2 PDF report
└── README.md                   # Project overview & documentation
```

---

## ⚙️ Quick Start & Execution

### 1. Environment Setup
```bash
cd CODE
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m spacy download en_core_web_sm
```

### 2. Run Task 1 Tokenization Pipeline
```bash
python3 src/tokenization.py
python3 src/evaluation.py
python3 src/error_analysis.py
```

### 3. Run Task 2 Normalization Pipeline
```bash
python3 src/task2_normalize.py
python3 src/task2_compare.py
```

---

## 🔗 Submission Links
- **GitHub Repository**: [https://github.com/tony19053000/Information-Retrieval-Assignment](https://github.com/tony19053000/Information-Retrieval-Assignment)
- **Detailed Report**: [IR_Assignment_Final_Report.md](IR_Assignment_Final_Report.md)

---

## 🤖 AI Usage Statement
In accordance with assignment guidelines: AI tools were used for code structuring, regex refinement, and report drafting. All datasets, metric evaluations, and normalization outputs were independently run and verified locally via Python scripts.
