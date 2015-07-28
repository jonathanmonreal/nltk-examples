# Jonathan Monreal

import nltk
from nltk.corpus import udhr

def find_language(word):
    all_languages = [language for language in udhr.fileids() if
                 language[-6:] == 'Latin1']
    word_languages = [language for language in all_languages if
                      word in udhr.words(language)]
    return word_languages
