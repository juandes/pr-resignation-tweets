import spacy
import re
import itertools
import numpy as np
import pandas as pd
from spacy import displacy


def top_pos(doc, pos, n, model_language):
    """Finds the top n spaCy pos

    Parameters:
    doc: spaCy's doc
    pos: pos we are interesting in finding; one of "VERB", "NOUN", "ADJ" or "ADV"
    n: how many pos
    """

    pos_count = {}
    for token in doc:
        # ignore stop words
        if token.is_stop:
            continue

        if token.pos_ == pos:
            if token.lemma_ in pos_count:
                pos_count[token.lemma_] += 1
            else:
                pos_count[token.lemma_] = 1

    # sort by values, but before get only those keys where value > 1;
    # I want lemmas that appear more than one
    # lastly, get the first n results
    result = sorted({k: v for (k, v) in pos_count.items() if v > 1}.items(),
                    key=lambda kv: kv[1], reverse=True)[:n]

    df = pd.DataFrame(result, columns=[pos, 'value'])
    df.to_csv('data/{}_{}.csv'.format(pos, model_language), header=True, index=False)

    print("top {} {} {}".format(n, pos, result))


def start_analysis(model_name, language):
    nlp = spacy.load(model_name)
    with open('data/cleaned_tweets_no_mentions_hashtags.txt', 'r') as file:
        text = file.read()

    nlp.max_length = len(text)

    doc = nlp(text)
    for i in ['VERB', 'NOUN', 'ADJ', 'ADV']:
        top_pos(doc, i, 30, language)


if __name__ == "__main__":
    start_analysis('es_core_news_md', 'Spanish')
    start_analysis('en_core_web_lg', 'English')
