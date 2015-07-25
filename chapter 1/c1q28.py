# Jonathan Monreal

from __future__ import division
import nltk

def percentage(word, text):
    return 100 * ([word.lower() for word in text].count(word)/len(text))
