import pandas as pd
import spacy
from nltk.tokenize import TweetTokenizer, word_tokenize

df = pd.read_csv("data/task1_ground_truth.csv")

tt = TweetTokenizer(
    preserve_case=True,
    reduce_len=False,
    strip_handles=False
)

nlp = spacy.load("en_core_web_sm")

def tweet_tokenize(text):
    return tt.tokenize(text)

def spacy_tokenize(text):
    return [token.text for token in nlp(text)]

def nltk_word_tokenize(text):
    return word_tokenize(text)

results = []

for i, row in df.iterrows():
    text = str(row["tweet"])

    results.append({
        "post_id": i + 1,
        "tweet": text,
        "tweet_tokenizer": tweet_tokenize(text),
        "spacy": spacy_tokenize(text),
        "nltk_word_tokenize": nltk_word_tokenize(text)
    })

out = pd.DataFrame(results)

out.to_csv(
    "results/tokenizer_results.csv",
    index=False
)

with open("results/tokenizer_output.txt", "w", encoding="utf-8") as f:
    for _, row in out.iterrows():
        f.write("=" * 80 + "\n")
        f.write(f"POST {row['post_id']}\n")
        f.write("=" * 80 + "\n\n")

        f.write("ORIGINAL:\n")
        f.write(row["tweet"] + "\n\n")

        f.write("GROUND TRUTH:\n")
        original = df.iloc[row["post_id"] - 1]

        f.write(f"Hashtags: {original['hashtags']}\n")
        f.write(f"Mentions: {original['mentions']}\n")
        f.write(f"URLs: {original['urls']}\n")
        f.write(f"Emojis: {original['emojis']}\n\n")

        f.write("NLTK TWEET TOKENIZER:\n")
        f.write(str(row["tweet_tokenizer"]) + "\n")
        f.write(f"Token count: {len(row['tweet_tokenizer'])}\n\n")

        f.write("SPACY:\n")
        f.write(str(row["spacy"]) + "\n")
        f.write(f"Token count: {len(row['spacy'])}\n\n")

        f.write("NLTK WORD TOKENIZE:\n")
        f.write(str(row["nltk_word_tokenize"]) + "\n")
        f.write(f"Token count: {len(row['nltk_word_tokenize'])}\n\n")

print("Tokenization complete.")
print("Posts processed:", len(out))
print("Saved:")
print("  results/tokenizer_results.csv")
print("  results/tokenizer_output.txt")