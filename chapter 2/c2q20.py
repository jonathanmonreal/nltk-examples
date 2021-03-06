# Jonathan Monreal

import nltk
from nltk.corpus import brown

# Implementation using FreqDist for illustration (slower, more memory use)
#def word_freq(word, section):
#    fdist = nltk.FreqDist(w.lower() for w in brown.words(categories=section))
#    try:
#        return fdist[word.lower()]
#    except:
#        return 0

def word_freq(word, section):
    try:
        return brown.words(categories=section).count(word)
    except:
        return 0
