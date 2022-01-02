from Student import Student
class Course:
    def __init__(self, num, name, max:int):
        if type(num) != int:
            raise TypeError
        if type(name) != str:
            raise TypeError
        if type(max) != int:
            raise TypeError
        self.num = num
        self.name = name
        self.subjects_teachers = {}
        self.students = []
        self.max_students = int(max)

    def __str__(self):
        return f"in course {self.num} {self.name} the subjects are: {self.subjects_teachers} and the students are: {self.students}, max students is: {self.max_students}"

    def add_student(self, student):
        if type(student) != Student:
            raise TypeError("only student can be added")
        if len(self.students) == self.max_students:
            print("there is no place!")
            return False
        if student in self.students:
            print("the student already exist!")
            return False
        self.students.append(student)
        return True

    def add_factor(self, subject, factor):
        if type(subject) != str:
            raise TypeError
        if type(factor) != int:
            raise TypeError
        if factor < 0:
            raise ValueError
        for i in self.students:
            i.calc_factor(subject, factor)

    def del_student(self, student):
        if type(student) != Student:
            raise TypeError("only student can be deleted")
        self.students.remove(student)

    def averages(self):
        sum = 0
        for i in self.students:
            sum += i.average()
        return sum/len(self.students)

    def weak_students(self):
        min_average = 100
        for i in self.students:
            if i.average() < min_average:
                min_average = i.average()
        indexes = []
        for i in range(len(self.students)):
            if self.students[i].average() == min_average:
                indexes.append(i)
        return indexes

