class Person:
    def __init__(self, name, age, num_of_kids):
        """function that builds the object Person"""
        self.name = name
        self.age = age
        self.num_of_kids = num_of_kids

    def __repr__(self):
        print('inside __repr__')
        return f"{self.name} age: {self.age} number of children: {self.num_of_kids}"

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

if __name__ == '__main__':
    #     main program
    my_person = Person('Matan', 21, 0)
    my_person.show()
    if my_person.hasChildren():
        print("has children")
    else:
        print("hasn't children")
    my_person.ageGroup()

    # list
    p1 = Person('Dani', 18, 0)
    p2 = Person('Gadi', 40, 2)
    p3 = Person('Shifra', 30, 1)
    list1 = [p1, p2, p3]
    print(list1[2])
    for i in list1:
        print(i)
    p1.height = 178
    print(p1)
