"""Question: Find the last word in every sentence"""

import re

sentence = "In ancient manuscripts, another means to divide sentences into paragraphs was a line break (newline) followed by an initial at the beginning of the next paragraph. An initial is an oversized capital letter, sometimes outdented beyond the margin of the text. This style can be seen, for example, in the original Old English manuscript of Beowulf. Outdenting is still used in English typography, though not commonly."


# Approach 1: Using split()

# Splitting the sentence based on the "." so we will get sentences strings
res = sentence.split(".")

# Looping over the sentances:
for i in range(0, len(res)):
    # Splitting the sentance so we will get a array of words
    # Printing last word in the sentance
    print(res[i].split(" ")[-1])


# Approach2: Using regex

# We will find the word which has "." at the end.
# "\w+" means variable which is the end of the word
# For matching the "." literally we have to use escape character "\"
# That's why we used "\."
regex = r"\w+\."

# findall will find every occurrence of the match
result = re.findall(regex, sentence)

final = []
for i in result:
    # removing the . from the word and adding it to empty array
    final.append(i.replace('.', ''))

print(f"Rsult using regex: {final}")
