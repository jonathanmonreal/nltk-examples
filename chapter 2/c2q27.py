# Jonathan Monreal

from __future__ import division
import nltk
from nltk.corpus import wordnet as wn

# part of speech = [(list of all synsets, part of speech abbreviation),
# list of all words in part of speech, polysemy]
nouns = [(list(wn.all_synsets(pos='n')), 'n'), [], 0]
verbs = [(list(wn.all_synsets(pos='v')), 'v'), [], 0]
adjectives = [(list(wn.all_synsets(pos='a')), 'a'), [], 0]
adverbs = [(list(wn.all_synsets(pos='r')), 'r'), [], 0]
part_of_speech = [nouns, verbs, adjectives, adverbs]

for part in part_of_speech:
    for synset in part[0][0]: # for each synset in all synsets for that part of speech
        part[1].append(str(synset)) # append the string of that synset

    # reduce synset string to only the word itself
    part[1] = [synset_name[8:synset_name.find('.')] for synset_name in part[1]]
    # reduce the list to the set of unique words
    part[1] = list(set(part[1]))

    for word in part[1]:    # for each word of that part of speech
        part[2] += len(wn.synsets(word, part[0][1])) # add the number of senses for the word
    part[2] /= len(part[1]) # average across the total number of words of that part of speech

print 'Part of Speech\tPolysemy'
print '================================'
print 'noun\t\t' + str(nouns[2])
print 'verb\t\t' + str(verbs[2])
print 'adjective\t' + str(adjectives[2])
print 'adverb\t\t' + str(adverbs[2])
