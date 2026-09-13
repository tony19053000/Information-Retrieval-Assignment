import pandas as pd
import re
from wordfreq import zipf_frequency

df = pd.read_csv("data/task2_posts.csv")

protected = re.compile(
    r'https?://[^\s]+|www\.[^\s]+|(?<!\w)#[A-Za-z0-9_]+|(?<!\w)@[A-Za-z0-9_]+|(?<!\w)\$[A-Za-z0-9_]+'
)

repeat = re.compile(r'([A-Za-z])\1{2,}')

def correct_word(word):
    if not repeat.search(word):
        return word

    candidates = set()

    for n in range(1, 3):
        candidate = re.sub(r'([A-Za-z])\1{2,}', lambda m: m.group(1) * n, word)
        candidates.add(candidate.lower())

    candidates.add(re.sub(r'([A-Za-z])\1{2,}', r'\1', word).lower())
    candidates.add(re.sub(r'([A-Za-z])\1{2,}', r'\1\1', word).lower())

    best = word.lower()
    best_score = zipf_frequency(best, "en")

    for candidate in candidates:
        score = zipf_frequency(candidate, "en")
        if score > best_score:
            best = candidate
            best_score = score

    if word.isupper():
        return best.upper()

    if word[0].isupper():
        return best.capitalize()

    return best

def normalize(text):
    saved = []

    def protect(match):
        saved.append(match.group(0))
        return f"__PROTECTED_{len(saved) - 1}__"

    temp = protected.sub(protect, str(text))

    words = re.split(r'(\s+)', temp)

    for i in range(0, len(words), 2):
        words[i] = correct_word(words[i])

    temp = ''.join(words)

    for i, value in enumerate(saved):
        temp = temp.replace(f"__PROTECTED_{i}__", value)

    return temp

df["normalized_tweet"] = df["tweet"].apply(normalize)

df.to_csv("data/task2_normalized.csv", index=False)

print("Posts processed:", len(df))
print("Saved to data/task2_normalized.csv")