
import unittest
from app import calculate_grade


class TestGradeCalculator(unittest.TestCase):

    def test_grade_a(self):
        self.assertEqual(calculate_grade(95), "A")

    def test_grade_b(self):
        self.assertEqual(calculate_grade(85), "B")

    def test_grade_f(self):
        self.assertEqual(calculate_grade(30), "F")

    def test_invalid_marks(self):
        self.assertEqual(calculate_grade(120), "Invalid Marks")


if __name__ == "__main__":
    unittest.main()
