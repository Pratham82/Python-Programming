
def Palindrome_Checker(str1):
    rev = ''
    for i in str1:
        rev = i + rev

    if rev == str1:
        print("Entered string is palindrome")
    else:
        print("Entered string is not palindrome")


entry = input("Enter string here: ")
Palindrome_Checker(entry)