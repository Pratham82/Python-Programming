"""
Say you have a file that contains some text. You need to count the number of times each letter appears in the text. For example, say you have a file called sample.txt
"""

from collections import Counter

sample_file = open('sample.txt', 'r')


def count_letters(fileName):
    letter_counter = Counter()
    for line in fileName:
        line_letters = [word for word in line.lower() if word.isalpha()]
        letter_counter.update(line_letters)
    return letter_counter


print(count_letters(sample_file))
