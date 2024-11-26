import unittest
from cmath import isclose
from main import find_roots

class TestFindRoots(unittest.TestCase):
    def test_two_real_roots(self):
        root1, root2 = find_roots(1, -5, 6)
        self.assertEqual(root1, 3.0)
        self.assertEqual(root2, 2.0)

    def test_one_real_root(self):
        root = find_roots(1, -4, 4)
        self.assertEqual(root, 2.0)

    def test_complex_roots(self):
        root1, root2 = find_roots(1, -2, 5)
        self.assertEqual(root1, complex(1, 2))
        self.assertEqual(root2, complex(1, -2))

    def test_invalid_a(self):
        with self.assertRaises(ValueError) as context:
            find_roots(0, 2, 3)
        self.assertEqual(str(context.exception), "Первый коэффициент не может быть равен нулю для квадратного уравнения")

    def test_invalid_types(self):
        with self.assertRaises(TypeError) as context:
            find_roots("aaaaaaaaaa", 2, 3)
        self.assertEqual(str(context.exception), "Коэффициенты должны быть числами")


    def test_large_numbers(self):
        roots = find_roots(9000000, 800000, 700000)
        self.assertTrue(all(isinstance(root, complex) for root in roots))
