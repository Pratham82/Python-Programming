"""
- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals
"""

animals = ["lion", "tiger", "fox", "elephant", "deer"]
animals.pop(3)
print(animals)
animals.append("monkey")
print(animals)
animals.pop(0)
print(animals)
print(animals[:3])
