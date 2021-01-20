for i in range(6):
    print(i * "*")

[print(i * "*") for i in range(6)]

print(
    """

      """
)

for i in range(6, 0, -1):
    print(i * "*")


print(
    """

      """
)

[print(i * "*") for i in range(5, 0, -1)]

print(
    """


      """
)


for i in range(1, 10):
    for j in range(10, i, -1):
        print(" ", end=" ")

    for k in range(1, i):
        print(" # ", end=" ")
    print(" ")
