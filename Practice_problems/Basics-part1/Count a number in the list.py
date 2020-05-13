# Taking values from users
input_1 = input("Enter number to add in the list: ")
list1 = input_1.split()
print(list1)

n = input("Enter the number to count in the list: ")

def count_nums(num):
    c =  0
    for i in list1:
        if n == i:
            c += 1

    print(f"count of {num}: {c}")

count_nums(n)
