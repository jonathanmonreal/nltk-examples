# Jonathan Monreal

import nltk
from nltk.corpus import udhr

def guess_language(raw):
    # tokenize raw text and get words
    tokens = nltk.wordpunct_tokenize(raw)
    words = [word.lower() for word in tokens if word.isalpha()]

    languages = ['French_Francais', 'German_Deutsch', 'Spanish_Espanol',
                 'English']
    guess = (None, 0) # used to store tuple with the guess

    for language in languages:
        file_words = udhr.words(fileids = language + '-Latin1')
        
        # only consider words that are in both the raw text and the udhr
        # for the language
        current = nltk.spearman_correlation(
                      nltk.FreqDist([word for word in words if word in
                                     file_words]),
                      nltk.FreqDist([word for word in file_words if
                                     word in words]))
        if current < guess[1]:
            guess = (language, current)

    return guess[0]

def example():
    print guess_language('The emphatic horse, cut short by the whip in a most '\
                         'decided negative, made a decided scramble for it, '\
                         'and the three other horses followed suit. Once '\
                         'more, the Dover mail struggled on, with the '\
                         'jack-boots of its passengers squashing along by its '\
                         'side. They had stopped when the coach stopped, and '\
                         'they kept close company with it. If ny one of the '\
                         'three had had a the hardihood to propose to another '\
                         'to walk on a little ahead into the mist and '\
                         'darkness, he would have put himself in a fair way '\
                         'of getting shot instantly as a highwayman.')
