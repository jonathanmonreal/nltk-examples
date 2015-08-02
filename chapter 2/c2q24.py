# Jonathan Monreal

from __future__ import division
import nltk
from nltk.corpus import brown
import random

# Part a
def generate_model(cfdist, word, num = 15):
    words = []
    
    for i in range(num):
        word = cfdist[word].max()
        words.append(word)

    return random.choice(words)

# Part b

print 'Part b:'

random_text = []
text = brown.words(categories = 'news')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)

for i in range(0, 5):
    random_text.append(generate_model(cfd, 'care'))
    random_text.append(generate_model(cfd, 'remember'))
    random_text.append(generate_model(cfd, 'noise'))

print(random_text)

# With all of the combinations I tried, I noticed that stopwords are very common
# among the randomly generated text, which isn't too surprising given that
# this model is based on most likely words. The text is fairly unintelligible.

# Part c

print 'Part c:'

random_text = []
words = ['care', 'try', 'see']
text2 = brown.words(categories = 'science_fiction')
bigrams2 = nltk.bigrams(text2)
cfd2 = nltk.ConditionalFreqDist(bigrams2)
cfds = [cfd, cfd2]

for i in range(0, 15):
    random_text.append(generate_model(random.choice(cfds), random.choice(words)))

print random_text

# The text is fairly unintelligible still, though it did manage to generate
# "I was first" as part of the text.
