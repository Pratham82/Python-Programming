def solve():
  inp = input()
  op = []
  for i in inp.split():
    op.append( i[0].upper() + i[1:])
  return(" ".join(op))

print(solve())

# print(solve('chrisalan'))


