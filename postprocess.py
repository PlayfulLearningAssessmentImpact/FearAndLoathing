#!/usr/bin/env python3

from pandas import read_csv
import spacy

nlp = spacy.load("model_ai_2/model-last")
def AI(text):
    return nlp(text).cats["AI"]

data = read_csv("sentences.csv")
data = data.sample(frac=1)[0:2000]
data["AI"] = data.Text.map(AI)
data.to_csv("coded.csv")