import pandas as pd
import re

df = pd.read_csv("data/task2_posts.csv")

pattern = r'([A-Za-z])\1{2,}'

with open("results/task2_repeated_patterns.txt", "w", encoding="utf-8") as f:
    for i, text in enumerate(df["tweet"].astype(str), 1):
        matches = re.findall(pattern, text)

        f.write(f"Post {i}\n")
        f.write(f"Original: {text}\n")
        f.write(f"Repeated characters: {matches}\n")
        f.write("-" * 80 + "\n")

print("Inspected:", len(df), "posts")
print("Saved to results/task2_repeated_patterns.txt")