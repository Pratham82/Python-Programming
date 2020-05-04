# Practice exercise

# Pig latin
# IF word starts with vowel add ay to end
# If word does not stat with a vowel put first letter at the end, then add ay

def pig_latin(word):
    if word[0] in  "aeiou":
        pig_word = word + 'ay'

    else: 
        pig_word = word[1:]+'ay'

    return pig_word 


print(pig_latin("hello"))


def lesser_of_two_evens(n,m):
    if n % 2==0 and m % 2==0:
        return min(n,m)
    else:
        return max(n,m)
     
print(lesser_of_two_evens(45,49))

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(word):
    words =word.split()
    # here [0][0] means 0th string after splitting and 0th position of the word
    return words[0][0] == words[1][0]

print(animal_crackers("Texas Ray"))


# LEVEL 1 PROBLEMS

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(word):
    if len(word) > 3:
        return word[:3].capitalize() + word[3:].capitalize()
    else:
        return "Entered name is too short"


print(old_macdonald("mcconaughey"))


# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(statement):
    splitted= statement.split()[::-1]
    return " ".join(splitted)


print(master_yoda("How you doin"))

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# Check ig if the difference between entered number and 100,200 is <=10 then print True or print false
def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

print(almost_there(101))
