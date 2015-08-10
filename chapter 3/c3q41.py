# Jonathan Monreal

words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious',
         'unidirectional']

vsequences = set([''.join([char for char in word if char in 'aeiou']) for word in words])
print sorted(vsequences)
