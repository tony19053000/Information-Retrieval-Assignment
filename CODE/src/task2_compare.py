import pandas as pd

df = pd.read_csv("data/task2_normalized.csv")

changed = df[df["tweet"] != df["normalized_tweet"]]

print("Total posts:", len(df))
print("Changed posts:", len(changed))
print("Unchanged posts:", len(changed))

print("\n" + "=" * 100)
print("BEFORE / AFTER EXAMPLES")
print("=" * 100)

for i, row in changed.head(25).iterrows():
    print("\nBEFORE:", row["tweet"])
    print("AFTER :", row["normalized_tweet"])
