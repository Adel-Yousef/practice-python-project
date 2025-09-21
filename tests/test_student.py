import unittest

from student.student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student("Adel")

    def test_create_student_object(self):
        # new_student = Student("Adel") we did it above
        self.assertEqual(self.student.name, "Adel")

    def test_add_valid_grade(self):
        self.student.add_grade(50)
        self.assertIn(50, self.student.grades)  # make sure 50 is in grades list
        self.student.add_grade(100)
        self.assertIn(100, self.student.grades) 
        self.student.add_grade(0)
        self.assertIn(0, self.student.grades) 

    def test_add_invalid_grade(self):
        with self.assertRaises(ValueError):
            self.student.add_grade(101)

        with self.assertRaises(TypeError):
            self.student.add_grade("hello")

        with self.assertRaises(ValueError):
            self.student.add_grade(-1)

    def test_average_no_grades(self):
        self.assertEqual(self.student.average(), 0)

    def test_average_with_grades(self):
        for grade in [20, 40, 60]:
            self.student.add_grade(grade)
        self.assertEqual(self.student.average(), 40)  # 20+40+60 = 120/3 = 40