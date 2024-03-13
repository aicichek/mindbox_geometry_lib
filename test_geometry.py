import unittest
from geometry import Circle, Triangle, calculate_area

class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(radius=5)
        self.assertAlmostEqual(calculate_area(circle), 78.53981633974483, places=5)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(calculate_area(triangle), 6)

    def test_right_angled_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angled())

if __name__ == '__main__':
    unittest.main()