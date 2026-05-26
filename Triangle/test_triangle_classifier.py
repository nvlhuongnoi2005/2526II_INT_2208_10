import unittest

from triangle_classifier import classify_triangle


class TestTriangleClassifier(unittest.TestCase):
    def test_invalid_input_below_lower_bound(self):
        self.assertEqual(classify_triangle(0, 1, 1), "Invalid Input")

    def test_invalid_input_above_upper_bound(self):
        self.assertEqual(classify_triangle(101, 50, 50), "Invalid Input")

    def test_invalid_input_non_integer(self):
        self.assertEqual(classify_triangle(3.5, 4, 5), "Invalid Input")

    def test_triangle_inequality_boundary(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Not a Triangle")

    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 1, 3), "Not a Triangle")

    def test_equilateral_min_boundary(self):
        self.assertEqual(classify_triangle(1, 1, 1), "Equilateral")

    def test_equilateral_max_boundary(self):
        self.assertEqual(classify_triangle(100, 100, 100), "Equilateral")

    def test_isosceles_ab(self):
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles")

    def test_isosceles_bc(self):
        self.assertEqual(classify_triangle(6, 7, 7), "Isosceles")

    def test_isosceles_ac(self):
        self.assertEqual(classify_triangle(9, 4, 9), "Isosceles")

    def test_scalene_valid_triangle(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

    def test_scalene_upper_boundary(self):
        self.assertEqual(classify_triangle(98, 99, 100), "Scalene")


if __name__ == "__main__":
    unittest.main()