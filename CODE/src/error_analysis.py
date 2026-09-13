import pandas as pd
import ast

ground = pd.read_csv("data/task1_ground_truth.csv")
results = pd.read_csv("results/tokenizer_results.csv")

tokenizers = {
    "NLTK TweetTokenizer": "tweet_tokenizer",
    "spaCy": "spacy",
    "NLTK Word Tokenize": "nltk_word_tokenize"
}

def parse(value):
    return ast.literal_eval(value)

with open("results/error_analysis.txt", "w", encoding="utf-8") as f:

    for name, column in tokenizers.items():

        f.write("=" * 100 + "\n")
        f.write(name + "\n")
        f.write("=" * 100 + "\n\n")

        for i in range(len(ground)):

            g = ground.iloc[i]
            r = results.iloc[i]

            tokens = parse(r[column])

            features = {
                "Hashtags": parse(g["hashtags"]),
                "Mentions": parse(g["mentions"]),
                "URLs": parse(g["urls"]),
                "Emojis": parse(g["emojis"])
            }

            errors = []

            for feature, items in features.items():

                for item in items:

                    if item not in tokens:
                        errors.append(
                            f"{feature}: {item}"
                        )

            if errors:

                f.write(f"POST {i + 1}\n")
                f.write("-" * 100 + "\n")
                f.write("Original:\n")
                f.write(g["tweet"] + "\n\n")

                f.write("Ground Truth:\n")
                f.write(f"Hashtags: {features['Hashtags']}\n")
                f.write(f"Mentions: {features['Mentions']}\n")
                f.write(f"URLs: {features['URLs']}\n")
                f.write(f"Emojis: {features['Emojis']}\n\n")

                f.write("Tokenizer Output:\n")
                f.write(str(tokens) + "\n\n")

                f.write("Errors:\n")

                for error in errors:
                    f.write(f"- {error}\n")

                f.write("\n")

print("Error analysis complete.")
print("Saved to: results/error_analysis.txt")