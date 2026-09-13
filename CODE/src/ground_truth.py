import pandas as pd
import re
import emoji

df = pd.read_csv("data/task1_posts.csv")

hashtag_re = re.compile(r"(?<!\w)#[A-Za-z0-9_]+")
mention_re = re.compile(r"(?<!\w)@[A-Za-z0-9_]+")
url_re = re.compile(r"https?://[^\s]+|www\.[^\s]+")

def extract_hashtags(text):
    return hashtag_re.findall(text)

def extract_mentions(text):
    return mention_re.findall(text)

def extract_urls(text):
    return url_re.findall(text)

def extract_emojis(text):
    return [x["emoji"] for x in emoji.emoji_list(text)]

df["hashtags"] = df["tweet"].astype(str).apply(extract_hashtags)
df["mentions"] = df["tweet"].astype(str).apply(extract_mentions)
df["urls"] = df["tweet"].astype(str).apply(extract_urls)
df["emojis"] = df["tweet"].astype(str).apply(extract_emojis)

df["hashtag_count"] = df["hashtags"].apply(len)
df["mention_count"] = df["mentions"].apply(len)
df["url_count"] = df["urls"].apply(len)
df["emoji_count"] = df["emojis"].apply(len)

df.to_csv("data/task1_ground_truth.csv", index=False)

print("Ground truth created.")
print("Posts:", len(df))
print("Hashtags:", df["hashtag_count"].sum())
print("Mentions:", df["mention_count"].sum())
print("URLs:", df["url_count"].sum())
print("Emojis:", df["emoji_count"].sum())

print("\nSaved to: data/task1_ground_truth.csv")