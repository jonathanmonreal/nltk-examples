# Jonathan Monreal

import nltk
from nltk.corpus import brown

text = brown.words(categories = 'news')[:50]

porter_stemmed = [nltk.PorterStemmer().stem(token) for token in text]
print porter_stemmed
print '\n\n'

lancaster_stemmed = [nltk.LancasterStemmer().stem(token) for token in text]
print lancaster_stemmed
