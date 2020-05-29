from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

# This will reset the position of the pointer to the start
def rewind(f):
    f.seek(0)

def print_a_line(line_no,f):
    print(line_no, f.readline())

current_file = open(input_file)

print("First print the whole file: ")
print_all(current_file)

print("Now let's rewind, Kind of like a tape: ")
rewind(current_file)

print("Lets print three lines: ")

current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_file.close()

