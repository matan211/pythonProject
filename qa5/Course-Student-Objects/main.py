from Student import Student
from Course import Course
# num_course = input("enter course number: ")
# name_course = input("enter course name: ")
# max_students = input("enter maximum amount of students: ")
num_course = '271'
name_course = 'qa'
max_students = 2
course = Course(num_course, name_course, max_students)
print(course)
course.subjects_teachers['biology'] = 'michal'
course.subjects_teachers['pysics'] = 'gadi'
print(course)
# while len(course.students) < course.max_students:
#     id = input("enter student id: ")
#     if id == '0':
#         break
#     else:
#         name = input('enter student name: ')
#         student = Student(id, name)
#         for i in course.subjects_teachers:
#             student.add_grade(i, int(input(f"enter grade for {student.name} in {i}: ")))
#         if not course.add_student(student):
#             break
matan = Student(211458484, 'Matan')
yuval = Student(123456789, 'Yuval')
matan.add_grade('biology', 80)
matan.add_grade('pysics', 80)
yuval.add_grade('biology', 50)
yuval.add_grade('pysics', 50)
course.add_student(matan)
course.add_student(yuval)
print(course)
# subject = input("enter subject for factor: ")
# factor = int(input("enter factor: "))
# course.add_factor(subject, factor)
course.add_factor('pysics', 10)
print(course)
for i in range(len(course.students)):
    if i in course.weak_students():
        course.del_student(course.students[i])
print(course)

