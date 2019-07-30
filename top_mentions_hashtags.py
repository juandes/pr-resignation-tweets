import re
import pandas as pd


def word_count_given_regex(str, regex, kind, n):
    counts = {}
    words = str.split()
    pattern = re.compile(regex)

    for word in words:
        match = pattern.search(word)
        if not match:
            continue
        matched = match.group(0)

        if matched in counts:
            counts[matched] += 1
        else:
            counts[matched] = 1

    result = sorted({k: v for (k, v) in counts.items() if v > 1}.items(),
                    key=lambda kv: kv[1], reverse=True)[:n]
    print(result)
    df = pd.DataFrame(result, columns=[kind, 'value'])
    df.to_csv('data/results/top_{}s.csv'.format(kind), header=True, index=False)

if __name__ == "__main__":
    with open('data/cleaned_tweets.txt', 'r') as file:
        text = file.read()
    word_count_given_regex(text, '@(\w+)+', 'mention', 10)
    word_count_given_regex(text, '#(\w+)+', 'hashtag', 10)
