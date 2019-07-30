import re

with open('data/tweets_no_location.txt', 'r') as file:
        text = file.read()

# remove RT mentions
text = re.sub('RT @[\w_]+:', '', text)

text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)

with open('data/cleaned_tweets.txt', 'w') as file:
    file.write(text)

text = re.sub('@[A-Za-z0-9]+', '', text)
with open('data/cleaned_tweets_no_mentions.txt', 'w') as file:
    file.write(text)

text = re.sub('#[A-Za-z0-9]+', '', text)
with open('data/cleaned_tweets_no_mentions_hashtags.txt', 'w') as file:
    file.write(text)
