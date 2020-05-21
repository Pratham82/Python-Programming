# Regular expressions are text-matching patterns described with a formal syntax. 

import re

patterns =['term1','term2']
text = 'This is a string with term1, but not the other term'

match1 = re.search('hello','hello world!')
print(match1)


# Text to parse
text = 'This is a string with term1, but it does not have the other term.'


for pattern in patterns:
    print('Searching for "%s" in:\n "%s"\n' %(pattern,text))
    
    #Check for match
    if re.search(pattern,text):
        print('Match was found. \n')
    else:
        print('No Match was found.\n')


# None will be returned when there is no match
print(re.search('h','a'))

matchobj = re.search(pattern,text)

print(type(matchobj))

# Split with reg expressions
split_term = '@' 
text = 'What is you email ID, is is dsfd@gmail.com?'

print(re.split(split_term,text))

# Finding instances of paterns
# This will retrun the list with all matches
# it will avoid the word if the casing was different
print(re.findall('match','This is testing text which have match, matcH'))

# re pattern syntax
def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %(pattern))
        print(re.findall(pattern,phrase))
        print('\n')
        
test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['sd*',         # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]




test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['[sd]',    # either s or d
                's[sd]+']   # s followed by one or more s or d

multi_re_find(test_patterns,test_phrase)


# Exclusions

# This can be used to remove punctuation form the sentence.
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print(re.findall('[^!.? ]+',test_phrase))

# Character Ranges

test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=['[a-z]+',      # sequences of lower case letters
               '[A-Z]+',      # sequences of upper case letters
               '[a-zA-Z]+',   # sequences of lower or upper case letters
               '[A-Z][a-z]+'] # one upper case letter followed by lower case letters

print(multi_re_find(test_patterns,test_phrase))


# Escape codes

test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

# For eliminating confusion between escape character and reg expressions we write
# r in at the starting of the patterns so in that way if \n or \t is passed it
# will be considered as normal string.
test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]

print(multi_re_find(test_patterns,test_phrase))