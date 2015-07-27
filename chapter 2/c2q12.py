# Jonathan Monreal

from __future__ import division
import nltk
from nltk.corpus import cmudict as cmu

entries = cmu.entries() # Stores the entries in the CMU dictionary
words = 0               # Stores the number of unique words
multiples = 0           # Stores the number of words with multiple pronunciations

for i in range(0, len(entries)):
    if entries[i-1][1] != entries[i][1]: # if the entry is a new word
        words += 1
    elif entries[i-1] != entries[i-2]:   # else if the word has a second pronunciation
        multiples += 1
        

print 'Words: ' + str(words)
print 'Multiples: ' + str(multiples)
