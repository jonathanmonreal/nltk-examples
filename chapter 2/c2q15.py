from __future__ import division
import nltk
from nltk.corpus import brown

fdist1 = nltk.FreqDist(brown.words())

for item in fdist1:
    if fdist1[item] > 2:
        print item
