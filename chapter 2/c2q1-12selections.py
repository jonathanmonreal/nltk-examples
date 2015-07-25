# Jonathan Monreal

from __future__ import division
import nltk
from nltk.corpus import gutenberg, brown, state_union

print ('2. len(gutenberg.words(\'austen-persuasion.txt\')) = ' +
       str(len(gutenberg.words('austen-persuasion.txt'))) + '\n')
print ('len(set([w.lower() for w in gutenberg.words(\'austen-persuasion.txt\')])) = ' +
       str(len(set([w.lower() for w in gutenberg.words('austen-persuasion.txt')]))) + '\n\n')

print ('3. brown.words(categories=\'news\') = ' + str(brown.words(categories='news')) + '\n')
print ('brown.words(categories=\'reviews\') = ' + str(brown.words(categories='reviews')) +
       '\n\n')

print ('4.\nfor fileid in state_union.fileids():\n    ' +
       'print str(state_union.words(fileid).count(\'men\')) + \' \' + ' +
       'str(state_union.words(fileid).count(\'women\')) + \' \' + ' +
       'str(state_union.words(fileid).count(\'people\'))')
print ('FileID\t\t\tMen\tWomen\tPeople')
print('===============================================')
for fileid in state_union.fileids():
    print (str(fileid) + ('\t' * (1 + int(2 - (1 / 15) * len(fileid)))) +
           str(state_union.words(fileid).count('men')) + '\t' +
           str(state_union.words(fileid).count('women')) + '\t' +
           str(state_union.words(fileid).count('people')))
print '\n\n'

print '5.'
for word in [wn.synset('aircraft.n.01'), wn.synset('zebra.n.01')]:
    print word
    print 'Member meronyms: ' + str(word.member_meronyms())
    print 'Part meronyms: ' + str(word.part_meronyms())
    print 'Substance meronyms: ' + str(word.substance_meronyms())
    print 'Member holonyms: ' + str(word.member_holonyms())
    print 'Part holonyms: " ' +  str(word.part_holonyms())
    print 'Substance holonyms: " ' +  str(word.substance_holonyms())
    print '\n'
print '\n\n'

