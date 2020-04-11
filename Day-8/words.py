# This i module docstring 
""" Retrieves and print words from a URL

Usage: 
    python words.py <url>
"""
import sys
from urllib.request import urlopen


# url ="http://sixty-north.com/c/t.txt"
def fetch_words(url):
    # This is function docstring which is documentation for function, modules and scripts
    """
    This module fetches words from URLs
    """
    story= urlopen(url)
    story_words= []

    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)

    story.close()
    return story_words

def print_items(items):
    for item in items:
        print(item)

# __name__: Specially named variable  allowing us to detect whether a module is 
# run as script or imported into another module

# print(__name__)

# python sets the value of __name__ differently depending how our module is being used

def main(url):
    #url = sys.argv[1]
    words= fetch_words(url)
    print_items(words)

if __name__ =="__main__":
    main(sys.argv[1])

