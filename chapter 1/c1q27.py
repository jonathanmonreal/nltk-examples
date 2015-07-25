# Jonathan Monreal

from __future__ import division
import nltk

def vocab_size(test):
    return len(set([word.lower() for word in text if word.isalpha()]))
