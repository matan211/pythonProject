class Student:
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade

    def checkPass(self):
        if 0 <= self.grade < 70:
            return False
        else:
            return True

    def updateGrade(self, factor):
        new_grade = self.grade*factor/100+self.grade
        if new_grade > 100:
            print("factor too big!")
            pass
        else:
            self.grade = new_grade

    def show(self):
        print(self.id)
        print(self.name)
        print(self.grade)

# =========================================================
# main
student = Student(211458484, 'Matan', 65)
if student.checkPass():
    print('passed')
else:
    print('failed')
student.updateGrade(10)
student.show()
