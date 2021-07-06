# Input:
# 1
# 1
# 1
# 2

if __name__ == '__main__':
    # Take the input in correct format
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Using for loop
    # final_list =[]
    # Iterate from x to z append the values into one list
    # for i in range(x + 1):
    #     for j in range(y + 1):
    #         for k in range(z + 1):
    # Only add the sublists whose sum is not equal to n
    #             if sum([i, j, k]) != n:
    #                 final_list.append([i, j, k])

    # Defining  Final list
    final_list = []

    # Create grid with the given values
    [[[final_list.append([i, j, k]) for k in range(z + 1)]
      for j in range(y + 1)] for i in range(x + 1)]

    # Only add the sublists whose sum is not equal to n
    last_list = [
        final_list[i] for i in range(len(final_list))
        if sum(final_list[i]) != n
    ]

    # Retun of print the modified list
    print([
        final_list[i] for i in range(len(final_list))
        if sum(final_list[i]) != n
    ])
