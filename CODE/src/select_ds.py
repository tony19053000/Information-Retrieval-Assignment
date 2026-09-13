import pandas as pd
import re
import emoji

df = pd.read_csv("data/Tesla.csv")

df = df[
    (df["language"].astype(str).str.lower() == "en") &
    (df["tweet"].notna())
].copy()

df = df.drop_duplicates(subset=["tweet"])

hashtag_re = re.compile(r"(?<!\w)#[A-Za-z0-9_]+")
mention_re = re.compile(r"(?<!\w)@[A-Za-z0-9_]+")
url_re = re.compile(r"https?://[^\s]+|www\.[^\s]+")

slang = {
    "lol", "lmao", "omg", "btw", "idk", "imo", "imho",
    "brb", "wtf", "thx", "pls", "plz", "u", "ur",
    "yep", "nah", "gonna", "wanna", "gotta", "rofl",
    "asap", "tbh", "rn", "dm", "irl", "jk"
}

def check_slang(text):
    words = re.findall(r"\b[\w']+\b", text.lower())
    return any(w in slang for w in words)

df["hashtag"] = df["tweet"].astype(str).apply(
    lambda x: bool(hashtag_re.search(x))
)

df["mention"] = df["tweet"].astype(str).apply(
    lambda x: bool(mention_re.search(x))
)

df["url"] = df["tweet"].astype(str).apply(
    lambda x: bool(url_re.search(x))
)

df["emoji"] = df["tweet"].astype(str).apply(
    lambda x: bool(emoji.emoji_list(x))
)

df["slang"] = df["tweet"].astype(str).apply(check_slang)

categories = ["hashtag", "mention", "url", "emoji", "slang"]

selected = []
covered = {c: 0 for c in categories}

remaining = df.copy()

# First prioritize posts that satisfy unmet requirements
while len(selected) < 50 and len(remaining) > 0:

    best_index = None
    best_score = -1

    for index, row in remaining.iterrows():

        score = 0

        for c in categories:
            if row[c] and covered[c] < 20:
                score += 1

        if score > best_score:
            best_score = score
            best_index = index

    if best_index is None:
        break

    row = remaining.loc[best_index]

    selected.append(row)

    for c in categories:
        if row[c]:
            covered[c] += 1

    remaining = remaining.drop(best_index)

# If fewer than 50 were selected, fill with other unique posts
if len(selected) < 50:
    extra = remaining.sample(
        n=min(50 - len(selected), len(remaining)),
        random_state=42
    )

    selected.extend([row for _, row in extra.iterrows()])

result = pd.DataFrame(selected).drop_duplicates(subset=["tweet"])

result = result.head(50)

result[["tweet"]].to_csv(
    "data/task1_posts.csv",
    index=False
)

print("English source posts:", len(df))
print("Final selected posts:", len(result))

print("\nRequirement coverage:")

print(
    "Hashtag posts:",
    result["tweet"].astype(str).apply(
        lambda x: bool(hashtag_re.search(x))
    ).sum()
)

print(
    "Mention posts:",
    result["tweet"].astype(str).apply(
        lambda x: bool(mention_re.search(x))
    ).sum()
)

print(
    "URL posts:",
    result["tweet"].astype(str).apply(
        lambda x: bool(url_re.search(x))
    ).sum()
)

print(
    "Emoji posts:",
    result["tweet"].astype(str).apply(
        lambda x: bool(emoji.emoji_list(x))
    ).sum()
)

print(
    "Slang/abbreviation posts:",
    result["tweet"].astype(str).apply(check_slang).sum()
)

print("\nSaved to: data/task1_posts.csv")