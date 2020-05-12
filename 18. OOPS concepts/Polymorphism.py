class Student():
    def __init__(self,name):
        self.name = name

    def speak(self):
        print (self.name, " is a student.")

Matt= Student("Matt")
Matt.speak()

class Teacher():
    def __init__(self,name):
        self.name = name

    def speak(self):
        print (self.name, " is a teacher.")


Lewis= Teacher("Lewis")
Lewis.speak()

print("-------------------------")
for person in [Matt, Lewis]:
    print(person)
    print(person.speak())

# Here we are passing the p1 argument which doesn't know what object is going to be passed
# Both Student and teacher class have the same method speak so it will work in both cases and calls respective class object.
def person_speak(p1):
    print(p1.speak())

person_speak(Matt)
person_speak(Lewis)
