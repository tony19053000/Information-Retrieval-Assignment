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

rows = []

for name, column in tokenizers.items():

    hashtag_total = 0
    hashtag_correct = 0
    mention_total = 0
    mention_correct = 0
    url_total = 0
    url_correct = 0
    emoji_total = 0
    emoji_correct = 0
    posts_with_hashtag_error = 0
    posts_with_mention_error = 0
    posts_with_url_error = 0
    posts_with_emoji_error = 0
    total_tokens = 0

    for i in range(len(ground)):

        g = ground.iloc[i]
        tokens = parse(results.iloc[i][column])

        hashtags = parse(g["hashtags"])
        mentions = parse(g["mentions"])
        urls = parse(g["urls"])
        emojis = parse(g["emojis"])

        hashtag_total += len(hashtags)
        mention_total += len(mentions)
        url_total += len(urls)
        emoji_total += len(emojis)

        hc = sum(x in tokens for x in hashtags)
        mc = sum(x in tokens for x in mentions)
        uc = sum(x in tokens for x in urls)
        ec = sum(x in tokens for x in emojis)

        hashtag_correct += hc
        mention_correct += mc
        url_correct += uc
        emoji_correct += ec

        if hc < len(hashtags):
            posts_with_hashtag_error += 1

        if mc < len(mentions):
            posts_with_mention_error += 1

        if uc < len(urls):
            posts_with_url_error += 1

        if ec < len(emojis):
            posts_with_emoji_error += 1

        total_tokens += len(tokens)

    rows.append({
        "Tokenizer": name,
        "Hashtag Preservation (%)": round(
            hashtag_correct / hashtag_total * 100, 2
        ) if hashtag_total else 0,
        "Mention Preservation (%)": round(
            mention_correct / mention_total * 100, 2
        ) if mention_total else 0,
        "URL Preservation (%)": round(
            url_correct / url_total * 100, 2
        ) if url_total else 0,
        "Emoji Preservation (%)": round(
            emoji_correct / emoji_total * 100, 2
        ) if emoji_total else 0,
        "Total Tokens": total_tokens,
        "Average Tokens per Post": round(
            total_tokens / len(ground), 2
        ),
        "Hashtag Error Posts": posts_with_hashtag_error,
        "Mention Error Posts": posts_with_mention_error,
        "URL Error Posts": posts_with_url_error,
        "Emoji Error Posts": posts_with_emoji_error
    })

summary = pd.DataFrame(rows)

summary.to_csv(
    "results/evaluation_summary.csv",
    index=False
)

print("\nFINAL TOKENIZATION EVALUATION")
print("=" * 100)
print(summary.to_string(index=False))

print("\n" + "=" * 100)
print("ASSIGNMENT ANSWERS")
print("=" * 100)

best_hashtag = summary.loc[
    summary["Hashtag Preservation (%)"].idxmax(),
    "Tokenizer"
]

best_emoji = summary.loc[
    summary["Emoji Preservation (%)"].idxmax(),
    "Tokenizer"
]

most_tokens = summary.loc[
    summary["Total Tokens"].idxmax(),
    "Tokenizer"
]

print("\n1. Best tokenizer for hashtags:")
print(best_hashtag)

print("\n2. Best tokenizer for emojis:")
print(best_emoji)

print("\n3. Tokenizer generating the most tokens:")
print(most_tokens)

print("\n4. Token counts:")
for _, row in summary.iterrows():
    print(
        f"{row['Tokenizer']}: "
        f"{row['Total Tokens']} total, "
        f"{row['Average Tokens per Post']} per post"
    )

print("\nSaved to: results/evaluation_summary.csv")