import re
sentance = "In ancient manuscripts, another means to divide sentences into paragraphs was a line break (newline) followed by an initial at the beginning of the next paragraph. An initial is an oversized capital letter, sometimes outdented beyond the margin of the text. This style can be seen, for example, in the original Old English manuscript of Beowulf. Outdenting is still used in English typography, though not commonly."


# Splitting the sentance based on the "."
res = sentance.split(".")

for i in range(0, len(res)):
    print(res[i].split(" ")[-1])


# Using regex
regex4 = r"\w+\."
result = re.findall(regex4, sentance)
final = []
for i in result:
    final.append(i.replace('.', ''))

print(f"Rsult using regex: {final}")
