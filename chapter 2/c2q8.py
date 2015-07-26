# Jonathan Monreal

from __future__ import division
import nltk
from nltk.corpus import names

print ('cfd = nltk.ConditionalFreqDist(\n' +
       '(fileid, name[-1])\n' +
       'for fileid in names.fileids()' +
       'for name in names.words(fileid))'
       )
cfd = nltk.ConditionalFreqDist(
    (fileid, name[0])
    for fileid in names.fileids()
    for name in names.words(fileid))
cfd.plot()
