import re

# dictionary to store the replacements
replacements = {'e':'3', 'i':'1', 'l':'|', 's':'5', '.':'5w33t!','ate':'8',
                '1':'ONEONE', 'o':'0', ' s':' $'}

def hacker(s):
    # normalize the text
    s = s.lower()
    s = re.sub(r'(\ss)|ate|[eiols\.]', replacement, s)
    print s

# gets the replacement to be used
def replacement(match):
    return replacements.get(match.group(0))
