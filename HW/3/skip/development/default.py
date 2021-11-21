
import pandas as pd
import spacy

'''
https://www.kaggle.com/pierremegret/gensim-word2vec-tutorial
'''
ddf = pd.read_csv('resource/csv/sample.csv')
df = df.dropna().reset_index(drop=True)
nlp = spacy.load('en')


