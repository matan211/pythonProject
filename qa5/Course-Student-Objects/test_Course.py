from unittest import TestCase
from Course import Course
from Student import Student


class TestCourse(TestCase):
    def setUp(self):
        self.course = Course(271, 'QA', 5)

    def test__init__valid(self):
        self.assertEqual(self.course.num, 271)
        self.assertEqual(self.course.name, 'QA')
        self.assertEqual(self.course.max_students, 5)

    def test__init__invalid(self):
        with self.assertRaises(TypeError):
            Course('271', 'qa', 5)
        with self.assertRaises(TypeError):
            Course(271, True, 5)
        with self.assertRaises(TypeError):
            Course(271, 'QA', 'aa')

    def test_add_student_valid(self):
        student = Student(211, 'Yossi')
        self.course.add_student(student)
        self.assertEqual(self.course.students.count(student), 1)

    def test_add_student_invalid(self):
        with self.assertRaises(TypeError):
            self.course.add_student(10)
        with self.assertRaises(TypeError):
            self.course.add_student()
        student = Student(211, 'Yossi')
        self.course.add_student(student)
        self.course.add_student(student)
        self.assertEqual(self.course.students.count(student), 1)

    def test_add_factor_valid(self):
        student1 = Student(211, 'Yossi')
        student2 = Student(322, 'Yam')
        student3 = Student(458, 'Yuval')
        student1.add_grade('Math', 80)
        student2.add_grade('Math', 90)
        student3.add_grade('Math', 95)
        self.course.add_student(student1)
        self.course.add_student(student2)
        self.course.add_student(student3)
        self.course.add_factor('Math', 10)
        self.assertEqual(student1.grades['Math'], 88)
        self.assertEqual(student2.grades['Math'], 99)
        self.assertEqual(student3.grades['Math'], 100)

    def test_add_factor_invalid(self):
        student1 = Student(211, 'Yossi')
        student2 = Student(322, 'Yam')
        student3 = Student(458, 'Yuval')
        student1.add_grade('Math', 80)
        student2.add_grade('Math', 90)
        student3.add_grade('Math', 95)
        self.course.add_student(student1)
        self.course.add_student(student2)
        self.course.add_student(student3)
        with self.assertRaises(ValueError):
            self.course.add_factor('English', 10)
        with self.assertRaises(ValueError):
            self.course.add_factor('Math', -1)
        with self.assertRaises(TypeError):
            self.course.add_factor('math', 'aa')
        with self.assertRaises(TypeError):
            self.course.add_factor(76, 10)

    def test_del_student_valid(self):
        student1 = Student(211, 'Yossi')
        student2 = Student(322, 'Yam')
        student3 = Student(458, 'Yuval')
        student1.add_grade('Math', 80)
        student2.add_grade('Math', 90)
        student3.add_grade('Math', 95)
        self.course.add_student(student1)
        self.course.add_student(student2)
        self.course.add_student(student3)
        self.course.del_student(student2)
        self.assertEqual(len(self.course.students), 2)

    def test_del_student_invalid(self):
        student1 = Student(211, 'Yossi')
        student2 = Student(322, 'Yam')
        student3 = Student(458, 'Yuval')
        student1.add_grade('Math', 80)
        student2.add_grade('Math', 90)
        student3.add_grade('Math', 95)
        self.course.add_student(student1)
        self.course.add_student(student2)
        self.course.add_student(student3)
        self.course.del_student(student2)
        with self.assertRaises(ValueError):
            self.course.del_student(student2)
        with self.assertRaises(TypeError):
            self.course.del_student('aaa')

    def test_averages(self):
        student1 = Student(211, 'Yossi')
        student2 = Student(322, 'Yam')
        student3 = Student(458, 'Yuval')
        student1.add_grade('Math', 80)
        student2.add_grade('Math', 90)
        student3.add_grade('Math', 95)
        student1.add_grade('English', 60)
        student2.add_grade('English', 78)
        student3.add_grade('English', 95)
        self.course.add_student(student1)
        self.course.add_student(student2)
        self.course.add_student(student3)
        self.assertEqual(self.course.averages(), 83)

    def test_weak_students(self):
        student1 = Student(211, 'Yossi')
        student2 = Student(322, 'Yam')
        student3 = Student(458, 'Yuval')
        student1.add_grade('Math', 80)
        student2.add_grade('Math', 70)
        student3.add_grade('Math', 95)
        student1.add_grade('English', 60)
        student2.add_grade('English', 70)
        student3.add_grade('English', 95)
        self.course.add_student(student1)
        self.course.add_student(student2)
        self.course.add_student(student3)
        self.assertTrue(self.course.weak_students() == [0, 1])
