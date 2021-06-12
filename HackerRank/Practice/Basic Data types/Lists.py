if __name__ == '__main__':
    N = int(input())
    l1 = []
    for i in range(0, N):
        command, *inputs = input().split(" ")
        if 'insert' == command:
            l1.insert(int(inputs[0]), int(inputs[1]))
        elif "remove" == command:
            value = int(inputs[0])
            l1.remove(value)
        elif "append" == command:
            value = int(inputs[0])
            l1.append(value)
        elif "sort" == command:
            l1.sort()
        elif "pop" == command:
            l1.pop()
        elif "reverse" == command:
            l1.reverse()
        elif 'print' == command:
            print(l1)
