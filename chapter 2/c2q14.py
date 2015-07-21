# Jonathan Monreal

from __future__ import division
from nltk.corpus import wordnet as wn

def supergloss(s):
    definitions = 'Definition of ' + str(s) + ': ' + str(s.definition()) + '\n'
    for hypernym in s.hypernyms():
        definitions += 'Definition of ' + str(hypernym) + ': ' + str(hypernym.definition()) + '\n'
    for hyponym in s.hyponyms():
        definitions += 'Definition of ' + str(hyponym) + ': ' + str(hyponym.definition()) + '\n'
    return definitions
