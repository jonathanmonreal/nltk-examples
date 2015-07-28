# Jonathan Monreal

from __future__ import division
import nltk
from nltk.corpus import stopwords

def bigram_freq(text):
    stopword_list = stopwords.words('english') # stores the stopwords
    # generate the frequency distribution for non-stopword bigrams
    fdist = nltk.FreqDist(nltk.bigrams([word.lower() for word in text if word.isalpha() and
                            word not in stopword_list]))
    # from the frequency distribution, get tuples with both the bigram and its frequency
    bigram_tuples = fdist.items()
    # sort the tuples based on bigram frequency
    bigram_tuples = sorted(bigram_tuples, key=lambda vocab: vocab[1])
    
    bigrams = [] # used to store the bigram list
    
    # reduce and sort the items
    for i in range(0, 50):
        try:
            bigrams.insert(0, bigram_tuples[i][0]) # store each item as it comes in at position 0
        except:
            break

    return bigrams
