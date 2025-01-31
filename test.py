import unittest
import main

class TestForOutsideDict(unittest.TestCase):
    def test_basic_case(self):
        result = main.forOutsideDict(10, 2, 2)
        expected = {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
        self.assertEqual(result, expected)

    def test_no_divisible(self):
        result = main.forOutsideDict(5, 3, 10)
        expected = {0: 0}
        self.assertEqual(result, expected)

    def test_empty_range(self):
        result = main.forOutsideDict(0, 2, 3)
        expected = {}
        self.assertEqual(result, expected)

    def test_power_zero(self):
        result = main.forOutsideDict(5, 0, 1)
        expected = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
        self.assertEqual(result, expected)

    def test_cond_one(self):
        result = main.forOutsideDict(5, 2, 1)
        expected = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
        self.assertEqual(result, expected)

    def test_large_input(self):
        result = main.forOutsideDict(1000, 1, 100)
        expected = {x: x for x in range(0, 1000, 100)}
        self.assertEqual(result, expected)

class TestForInsideDict(unittest.TestCase):
    def test_basic_case(self):
        result = main.forInsideDict(10, 2, 2)
        expected = {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
        self.assertEqual(result, expected)

    def test_no_divisible(self):
        result = main.forInsideDict(5, 3, 10)
        expected = {0: 0}
        self.assertEqual(result, expected)

    def test_empty_range(self):
        result = main.forInsideDict(0, 2, 3)
        expected = {}
        self.assertEqual(result, expected)

    def test_power_zero(self):
        result = main.forInsideDict(5, 0, 1)
        expected = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
        self.assertEqual(result, expected)

    def test_cond_one(self):
        result = main.forInsideDict(5, 2, 1)
        expected = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
        self.assertEqual(result, expected)

    def test_large_input(self):
        result = main.forInsideDict(1000, 1, 100)
        expected = {x: x for x in range(0, 1000, 100)}
        self.assertEqual(result, expected)


class TestForOutside(unittest.TestCase):
    def test_basic_case(self):
        result = main.forOutside(10, 2, 2)
        expected = [0, 4, 16, 36, 64]
        self.assertEqual(result, expected)

    def test_no_divisible(self):
        result = main.forOutside(5, 3, 10)
        expected = [0]
        self.assertEqual(result, expected)

    def test_empty_range(self):
        result = main.forOutside(0, 2, 3)
        expected = []
        self.assertEqual(result, expected)

    def test_power_zero(self):
        result = main.forOutside(5, 0, 1)
        expected = [1, 1, 1, 1, 1]
        self.assertEqual(result, expected)

    def test_cond_one(self):
        result = main.forOutside(5, 2, 1)
        expected = [0, 1, 4, 9, 16]
        self.assertEqual(result, expected)

    def test_large_input(self):
        result = main.forOutside(1000, 1, 100)
        expected = [x for x in range(0, 1000, 100)]
        self.assertEqual(result, expected)


class TestForInside(unittest.TestCase):
    def test_basic_case(self):
        result = main.forInside(10, 2, 2)
        expected = [0, 4, 16, 36, 64]
        self.assertEqual(result, expected)

    def test_no_divisible(self):
        result = main.forInside(5, 3, 10)
        expected = [0]
        self.assertEqual(result, expected)

    def test_empty_range(self):
        result = main.forInside(0, 2, 3)
        expected = []
        self.assertEqual(result, expected)

    def test_power_zero(self):
        result = main.forInside(5, 0, 1)
        expected = [1, 1, 1, 1, 1]
        self.assertEqual(result, expected)

    def test_cond_one(self):
        result = main.forInside(5, 2, 1)
        expected = [0, 1, 4, 9, 16]
        self.assertEqual(result, expected)

    def test_large_input(self):
        result = main.forInside(1000, 1, 100)
        expected = [x for x in range(0, 1000, 100)]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()