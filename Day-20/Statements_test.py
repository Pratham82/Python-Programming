# Use for, .split(), and if to create a Statement that will print out words that start with 's':
print("Challenge 1 : ")
st = 'Print only the words that start with s in this sentence'

for word in st.split():
    if word[0]=='s' or word[0]=='S':
        print(word)


# Use range() to print all the even numbers from 0 to 10.
l1= list(range(0,11,2))
print(l1)

for num in range(0,11,2):
    print(num)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print("Challenge 3 : ")

list1 =[i for i in range(1,51) if i%3==0]
print(list1)

# Go through the string below and if the length of a word is even print "even!"

st1 = 'Print every word in this sentence that has an even number of letters'
print("Challenge 4 : ")
for i in st1.split():
    if len(i) %2==0:
        print(f"{i}: even")

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for n in range(1,101):
    if n % 3==0 and n % 5== 0:
        print("FizzBuzz")
    elif n % 3 ==0:
        print("Fizz")
    elif n % 5 ==0:
        print("Buzz")
    else:
        print(n)

# Use List Comprehension to create a list of the first letters of every word in the string below:

st2 = 'Create a list of the first letters of every word in this string'

list1 =[ i[0] for i in st2.split()]

print(list1)