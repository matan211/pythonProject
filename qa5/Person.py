class Person:
    def __init__(self, name, age, num_of_kids):
        """function that builds the object Person"""
        self.name = name
        self.age = age
        self.num_of_kids = num_of_kids

    def show(self):
        """prints the parameters"""
        print(self.name)
        print(self.age)
        print(self.num_of_kids)

    def hasChildren(self):
        if self.num_of_kids > 0:
            return True
        else:
            return False

    def ageGroup(self):
        if 0 <= self.age <= 18:
            print("Child")
        elif 19 <= self.age <= 60:
            print("Adult")
        elif 61 <= self.age <= 120:
            print("Senior")


#     main program
my_person = Person('Matan', 21, 0)
my_person.show()
if my_person.hasChildren():
    print("has children")
else:
    print("hasn't children")
my_person.ageGroup()
