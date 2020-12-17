# Count the occurence of number

list1 = []


def count_occurence(list):
    print(
        """
          #########################################
          WELCOME TO THE DBS CONSOLE
          #########################################
          """
    )

    n = int(input("Input the number of elements to be stored in the list: "))
    print(f"Input {n} numbers in the list")

    for i in range(n):
        var1 = int(input(f"element - {i}: "))
        list.append(var1)

    unrepeated = set(list)

    print("The frequency of all elements of the list: ")
    for i in unrepeated:
        print(f"{i} occurs {list.count(i)} times")


count_occurence(list1)
