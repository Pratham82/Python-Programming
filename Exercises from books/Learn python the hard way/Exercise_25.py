def break_words(word):
    """This fucntion will break words for us."""
    words = word.split()
    return words

def sort_words(words):
    """Sorts the words,"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """ Print the last word after popping it off"""
    word =  words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in full sentence and returns sorterd words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last word in the sentence"""
    words =  break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sort the words then prints the first and last one"""
    words = sort_sentance(sentence)
    print_first_word(words)
    print_last_word(words)

    
