from unittest import TestCase
from Student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student(211, 'Yossi')

    def test__init__valid(self):
        self.assertEqual(self.student.id, 211)
        self.assertEqual(self.student.name, 'Yossi')
        self.assertEqual(self.student.grades, {})

    def test__init__invalid(self):
        with self.assertRaises(TypeError):
            Student("aaa", "Yossi")
        with self.assertRaises(TypeError):
            Student(211, 56)
        with self.assertRaises(TypeError):
            Student("aaa", 56)
        with self.assertRaises(TypeError):
            Student("", )

    def test_add_grade_valid(self):
        self.student.add_grade('English', 80)
        self.student.add_grade('Math', 100)
        self.student.add_grade('Biology', 0)
        self.assertEqual(self.student.grades['English'], 80)
        self.assertEqual(self.student.grades['Math'], 100)
        self.assertEqual(self.student.grades['Biology'], 0)

    def test_add_grade_invalid(self):
        with self.assertRaises(TypeError):
            self.student.add_grade(211, 80)
        with self.assertRaises(TypeError):
            self.student.add_grade('English', 'aaa')
        with self.assertRaises(TypeError):
            self.student.add_grade(211, 'aaa')
        with self.assertRaises(ValueError):
            self.student.add_grade('English', -1)
        with self.assertRaises(ValueError):
            self.student.add_grade('English', 101)
        self.student.add_grade('Math', 80)
        self.student.add_grade('Math', 100)
        self.assertEqual(self.student.grades['Math'], 80)

    def test_calc_factor_valid(self):
        self.student.add_grade('Math', 80)
        self.student.calc_factor('Math', 0)
        self.assertEqual(self.student.grades['Math'], 80)
        self.student.calc_factor('Math', 25)
        self.assertEqual(self.student.grades['Math'], 100)

    def test_calc_factor_invalid(self):
        self.student.add_grade('Math', 80)
        with self.assertRaises(TypeError):
            self.student.calc_factor('English', 'aa')
        with self.assertRaises(TypeError):
            self.student.calc_factor(211, 80)
        with self.assertRaises(TypeError):
            self.student.calc_factor(211, 'aa')
        with self.assertRaises(ValueError):
            self.student.calc_factor('Math', -1)
        with self.assertRaises(ValueError):
            self.student.calc_factor('Math', -1)
        with self.assertRaises(ValueError):
            self.student.calc_factor('English', 10)

    def test_average(self):
        self.student.add_grade('Math', 80)
        self.student.add_grade('English', 100)
        self.assertEqual(self.student.average(), 90)

    def test__eq__invalid(self):
        with self.assertRaises(TypeError):
            self.student == 10
        with self.assertRaises(TypeError):
            self.student == 'aa'

    def test__eq__false(self):
        other = Student(322, 'Yam')
        self.assertFalse(self.student == other)
        other = Student(322, 'Yossi')
        self.assertFalse(self.student == other)

    def test__eq__true(self):
        other = Student(211, 'Yam')
        self.assertTrue(self.student == other)
        other = Student(211, 'Yossi')
        self.assertTrue(self.student == other)
