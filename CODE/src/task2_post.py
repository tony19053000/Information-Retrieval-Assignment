import pandas as pd
import re

df = pd.read_csv("data/Tesla.csv")
task1 = pd.read_csv("data/task1_posts.csv")

df = df.dropna(subset=["tweet"])
df["tweet"] = df["tweet"].astype(str)

task1_texts = set(task1["tweet"].astype(str))

df = df[~df["tweet"].isin(task1_texts)]
df = df.drop_duplicates(subset=["tweet"])

pattern = r'([A-Za-z])\1{2,}'

df = df[df["tweet"].str.contains(pattern, regex=True, na=False)]

print("Available posts with repeated characters:", len(df))

if len(df) < 100:
    print("There are fewer than 100 matching posts.")
else:
    task2 = df.sample(n=100, random_state=42)
    task2[["tweet"]].to_csv("data/task2_posts.csv", index=False)
    print("Task 2 posts selected:", len(task2))
    print("Saved to data/task2_posts.csv")