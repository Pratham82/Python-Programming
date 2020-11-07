# The Python KeyError is a type of LookupError exception and denotes that there was an issue retrieving the key you were looking for. When you see a KeyError

# KeyError
scores = {"Joey": 45, "Ross": 85, "Chandler": 80}

# Taking name of student
student = input("Get age for: ")
score = scores.get(student)

# Without excpetion handling
# This line will create Key error if the Key is not present in dcictionary
# print(scores[student])
# print(f"Socre of {student} is  {score}")

# With exception handling
# Exception hanlding
try:
    print(scores[student])
except KeyError:
    print(f"{student}'s score is unknown'")
