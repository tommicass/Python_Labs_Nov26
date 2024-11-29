
import basic
import unittest

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(basic.add(4, 3), 7, "Error should be 7")
        self.assertEqual(basic.add(4, 3, 2), 9, "Error should be 9")
        return None

    def test_mul(self):
        self.assertEqual(basic.mul(4, 3), 13, "Error should be 13")
        self.assertEqual(basic.mul(4, 3, 2), 24, "Error should be 24")
        return None

    def test_div(self):
        self.assertEqual(basic.div(4, 3), 1.334, "Error should be 1.334")
        return None


if __name__ == "__main__":
    unittest.main()