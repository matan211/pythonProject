class Student:
    def __init__(self, id: int, name: str):
        if type(id) != int:
            raise TypeError
        if type(name) != str:
            raise TypeError
        self.id = id
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        if type(grade) != int:
            raise TypeError
        if type(subject) != str:
            raise TypeError
        if grade < 0 or grade > 100:
            raise ValueError
        if subject not in self.grades:
            self.grades[subject] = grade

    def __str__(self):
        return f"the grades of {self.id} {self.name} are: {self.grades}"

    def __repr__(self):
        return f"the grades of {self.id} {self.name} are: {self.grades}"

    def calc_factor(self, subject, factor):
        if type(factor) != int:
            raise TypeError
        if type(subject) != str:
            raise TypeError
        if subject not in self.grades:
            raise ValueError
        if factor < 0:
            raise ValueError
        new_grade = self.grades[subject] * factor / 100 + self.grades[subject]
        if new_grade > 100:
            new_grade = 100
        self.grades[subject] = new_grade


    def average(self):
        sum = 0
        for i in self.grades:
            sum += self.grades[i]
        return sum/len(self.grades)

    def __eq__(self, other):
        if type(other) != Student:
            raise TypeError("only student type")
        if self.id == other.id:
            return True
        else:
            return False
# main
if __name__ == "__main__":
    s = Student(211, 'Matan')
    s.add_grade('biology', 80)
    print(s)
    s.calc_factor('biology', 10)
    print(s)
    s.add_grade('Math', 70)
    s.add_grade('Chemistry', 83)
    print(s)
    average = s.average()
    print(average)
