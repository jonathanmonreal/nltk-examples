# Jonathan Monreal

words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious',
         'unidirectional']

# method not using str translate() method
def method_one():
    for i in range(0, len(words)):
        # takes each string and separates it into a list of characters
        words[i] = list(words[i])
        for char in words[i]:
            if char not in 'aeiou':
                char = ''
        words[i] = ''.join(words[i])
    print sorted(words)

# method using the built in str translate() method
def method_two():
    for i in range(0, len(words)):
        # uses translate to replace consonants with nothing
        words[i] = words[i].translate(None, 'bcdfghjklmnpqrstvwxyz')
    print sorted(words)
