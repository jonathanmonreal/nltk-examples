# Jonathan Monreal

from __future__ import division
from nltk.book import *

print '1. 12 / (4 + 1) = ' + str(12 / (4 + 1)) + '\n\n'

print '2. 26 ** 100 = ' + str(26 ** 100) + '\n\n'

print '3. [\'Monty\', \'Python\'] * 20 =\n' + str(['Monty', 'Python'] * 20) + '\n'
sent1 = ['Call', 'me', 'Ishmael', '.']
print '3 * sent1 =\n' + str(['Call', 'me', 'Ishmael', '.'] * 3) + '\n\n'

print ('4. len([word.lower() for word in text1 if word.isalpha()]) = ' +
       str(len([word.lower() for word in text1 if word.isalpha()])) + '\n')
print ('len(set([word.lower() for word in text1 if word.isalpha()])) = ' +
       str(len(set([word.lower() for word in text1 if word.isalpha()]))) + '\n\n')

print '7. text5.collocations()\n'
print str(text5.collocations()) + '\n\n'

print '10. my_sent = ["This", "is", "a", "sentence"]\n'
my_sent = ["This", "is", "a", "sentence"]
print '\' \'.join(my_sent) = ' + str(' '.join(my_sent) + '\n')
print '\'This is a sentence\'.split() = ' + str('This is a sentence'.split()) + '\n\n'

print '14. sent3[2:].index(\'the\') = ' + str(sent3[2:].index('the') + 2) + '\n'
print 'sent3[6:].index(\'the\') = ' + str(sent3[6:].index('the') + 6) + '\n\n'

print ('15. sorted(set([word.lower() for word in text5 if word.isalpha() and word.startswith(\'b\')])' +
       " = " + str(sorted(set([word.lower() for word in text5 if word.isalpha() and word.startswith('b')]))) +
       '\n\n')

print '17. text9.index(\'sunset\') = ' + str(text9.index('sunset')) + '\n'
print 'text9[621:644] = ' + str(text9[621:644]) + '\n\n'

