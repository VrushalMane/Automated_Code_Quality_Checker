
import unittest
import runpy
from unittest.mock import patch

from app import calculate_grade


class TestGradeCalculator(unittest.TestCase):

    # Grade Tests

    def test_grade_a(self):
        self.assertEqual(calculate_grade(95), "A")

    def test_grade_b(self):
        self.assertEqual(calculate_grade(85), "B")

    def test_grade_c(self):
        self.assertEqual(calculate_grade(65), "C")

    def test_grade_d(self):
        self.assertEqual(calculate_grade(45), "D")

    def test_grade_f(self):
        self.assertEqual(calculate_grade(30), "F")

    # Boundary Tests

    def test_grade_a_boundary(self):
        self.assertEqual(calculate_grade(90), "A")

    def test_grade_b_boundary(self):
        self.assertEqual(calculate_grade(75), "B")

    def test_grade_c_boundary(self):
        self.assertEqual(calculate_grade(60), "C")

    def test_grade_d_boundary(self):
        self.assertEqual(calculate_grade(40), "D")

    # Special Cases

    def test_zero_marks(self):
        self.assertEqual(calculate_grade(0), "F")

    def test_maximum_marks(self):
        self.assertEqual(calculate_grade(100), "A")

    def test_invalid_marks(self):
        self.assertEqual(calculate_grade(120), "Invalid Marks")

    # Main Program Execution Test

    def test_main_execution(self):
        with patch("builtins.print") as mock_print:
            runpy.run_path("app.py", run_name="__main__")

        self.assertEqual(mock_print.call_count, 4)

        mock_print.assert_any_call("B")
        mock_print.assert_any_call("F")
        mock_print.assert_any_call("Invalid Marks")
        mock_print.assert_any_call("C")


if __name__ == "__main__":
    unittest.main()
