class Course:
    def __init__(self, course_num, course_name, students, max_students):
        self.course_num = course_num
        self.course_name = course_name
        self.students = students
        self.max_students = max_students

    def __str__(self):
        return (
            f"course number: {self.course_num}, name: {self.course_name}, number of students: {self.students}, maximum students: {self.max_students}")

    def howManyLeft(self):
        return (self.max_students - self.students)

    def addStudents(self, new):
        if self.students + new > self.max_students:
            print("too many")
        else:
            self.students += new


# main
c1 = Course(1132, 'QA', 100, 150)
print(c1)
c1.addStudents(20)
print(c1)
c1.addStudents(40)
print(c1)
