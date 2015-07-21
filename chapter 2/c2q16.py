# Jonathan Monreal

from __future__ import division
import nltk
from nltk.corpus import brown

def lexical_diversity(text):
    return len(text) / len(set(text))

fdists = []

print 'Category\tTokens\tTypes\tLexical diversity'
print '================================================='
for category in brown.categories():
    print (category + ('\t' * (1 + int(2 - (1 / 7) * len(category)))) + str(len(brown.words(categories=category))) + 
    '\t' + str(len(set(brown.words(categories=category)))) + '\t' + str(lexical_diversity(brown.words(categories=category))))
