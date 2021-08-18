def swap_case(s):
  new_arr = []
  for i in s:
    if i == i.upper():
      new_arr.append(i.lower())
    elif i == i.lower():
      new_arr.append(i.upper())
  return "".join(new_arr)


# print(swap_case('HackerRank.com presents'))
print(swap_case('HackerRank.com presents "Pythonist 2".'))