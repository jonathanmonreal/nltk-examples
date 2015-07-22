# Jonathan Monreal

import nltk
from nltk.corpus import brown

def word_freq(word, section):
    fdist = nltk.FreqDist(w.lower() for w in brown.words(categories=section))
    try:
        return fdist[word.lower()]
