import test
print("Top level in test.py")

test.myFun()


if __name__ == "__main__":
    print("test2.py is running directly")
else:
    print("test2.py is imported")
