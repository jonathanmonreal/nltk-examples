# Jonathan Monreal

from __future__ import division
import nltk
from nltk.corpus import stopwords

def freq_nonstop(text):
    stopword_list = stopwords.words('english') # stores the stopwords
    # generate the frequency distribution for non-stopwords
    fdist = nltk.FreqDist([word.lower() for word in text if word.isalpha() and
                            word not in stopword_list])
    # from the frequency distribution, get tuples with both the word and its frequency
    vocabulary_tuples = fdist.items()
    # sort the tuples based on the word frequency
    vocabulary_tuples = sorted(vocabulary_tuples, key=lambda vocab: vocab[1])
    
    vocabulary = [] # used to store the vocabulary
    
    # reduce and sort the items
    for i in range(0, 50):
        try:
            vocabulary.insert(0, vocabulary_tuples[i][0]) # store each item as it comes in at position 0
        except:
            break

    return vocabulary
