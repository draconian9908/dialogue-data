## THIS FILE IS NOT USED! USE analysis_vs.py INSTEAD!


## Analysis of the data gathered: sentiment analysis of dialogue and its relation to gender.
import numpy as np
import pandas as pd
import nltk
import matplotlib.pyplot as plt

nltk.download('punkt')

long_path = './data/'
f = open(long_path + "Horror_data.csv")
df = pd.read_csv(f)


def make_token(para):
    # substitute in a regular apostrophe for '’' to word with word_tokenize
    tokens = nltk.tokenize.word_tokenize(para)
    words = list(filter(lambda w: any(x.isalpha() for x in w), tokens))
    return " ".join(words)

def trigrams(s):
  seq = [s[i:] for i in range(3)]
  ngrams = zip(*seq)
  return [" ".join(ngram) for ngram in ngrams]


tokens = df['dialogue'].map(make_token)
trigrams = ngrams(tokens)
