# Jonathan Monreal

from __future__ import division
import nltk
from textwrap import fill

s = 'colorless'
print '1. s = \'colorless\''
s = s[:4] + 'u' + s[4:]
print 's = s[:4] + \'u\' + s[4:]'
print 's: ' + s
print '\n\n'

print '2. \'dishes\'[:-2]: ' + 'dishes'[:-2]
print '\'running\'[:-4]: ' + 'running'[:-4]
print '\'nationality\'[:-5]: ' + 'nationality'[:-5]
print '\'undo\'[:-2]: ' + 'undo'[:-2]
print '\'preheat\'[:-4]: ' + 'preheat'[:-4]
print '\n\n'

print '3. Yes. You can only wrap around once using negative values. Example: '\
      '\'lol\'[-4]'

monty = 'monty python'
print '5. monty[::-1]: ' + monty[::-1]
print fill('The string is printed backwards. This is a reasonable result given that'\
      '[:] specifies the entire string, and using -1 as the step steps through'\
      ' the string backwards.')
print '\n\n'

print '7.'
print 'a. Using NLTK: r\'<a|an|the>\'; Otherwise: r\'\s(a|an|the)\s\''
print '\n\n'

raw = 'this is a test string I am going to split around the character a'
print '11. raw = \'this is a test string I am going to split around the '\
      'character a\''
print 'raw.split(\'a\'): ' + str(raw.split('a'))
print '\n\n'

test_string = 'this\t\t \tis a test string'
print '13. test_string = \'this\t\t \tis a test string\''
print 'test_string.split(): ' + str(test_string.split())
print 'test_string.split(\' \'): ' + str(test_string.split(' '))
print fill('Using .split() ignores all whitespace characters, while using'\
      '.split(\' \') does not.')
print '\n\n'
