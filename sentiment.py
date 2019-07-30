import pandas as pd
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

client = language.LanguageServiceClient()

document = types.Document(
           gcs_content_uri='gs://gcp-bucket/file.txt',
           type=enums.Document.Type.PLAIN_TEXT)

annotations = client.analyze_sentiment(document=document,
                                       encoding_type='UTF32', timeout=600)

sentences = []
for s in annotations.sentences:
    sentences.append((s.text.content, s.sentiment.score, s.sentiment.magnitude))

df = pd.DataFrame(sentences, columns=['sentence', 'score', 'magnitude'])
df.to_csv('data/sentences_sentiment.csv')
