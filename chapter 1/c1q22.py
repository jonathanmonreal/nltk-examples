# Jonathan Monreal

from __future__ import division
import nltk
from nltk.book import *

# generate the frequency distribution
fdist5 = nltk.FreqDist([word.lower() for word in text5 if word.isalpha() and len(word) == 4])
# from the frequency distribution, get tuples with both the word and its frequency
vocabulary5_tuples = fdist5.items()
# sort the tuples based on the word frequency
vocabulary5_tuples = sorted(vocabulary5_tuples, key=lambda vocab: vocab[1])

vocabulary5 = [] # used to store the vocabulary

# reduce and sort the items
for item in vocabulary5_tuples:
    vocabulary5.insert(0, item[0]) # store each item as it comes in at position 0

print vocabulary5
