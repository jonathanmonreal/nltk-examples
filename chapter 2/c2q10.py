# Jonathan Monreal

from __future__ import division
import nltk
from nltk.book import *

def percentage(word, text):
    return 100 * ([word.lower() for word in text].count(word)/len(text))

# generate the frequency distribution
fdist5 = nltk.FreqDist([word.lower() for word in text5 if word.isalpha() and len(word) == 4])
# from the frequency distribution, get tuples with both the word and its frequency
vocabulary5_tuples = fdist5.items()
# sort the tuples based on the word frequency
vocabulary5_tuples = sorted(vocabulary5_tuples, key=lambda vocab: vocab[1])

percent = 0 # stores the percentage so far
words = []  # stores the words that account for 30%

# goes through the tuples starting from the most frequent word
for i in range(len(vocabulary5_tuples) - 1, 0, -1):
    if percent <= 33: # if less than 1/3 of the words have been accounted for
        words.append(vocabulary5_tuples[i][0])
        percent += percentage(vocabulary5_tuples[i], text5)
    else:
        break

print words
