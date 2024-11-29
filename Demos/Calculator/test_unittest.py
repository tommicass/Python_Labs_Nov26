#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This script will demo
"""
Docstring
"""

import Basic as basic
import unittest as ut

class TestCalc(ut.TestCase):
    def test_add(self):
        self.assertEqual(basic.add(4, 3), 7, "Error - should be 7")
        self.assertEqual(basic.add(4, 3, 2), 9, " Error - should be 9")
        return None

    def test_mul(self):
        self.assertEqual(basic.mul(4, 3), 12, "Error - should be 12")
        self.assertEqual(basic.mul(4, 3, 2), 24, " Error - should be 24")
        return None

    def test_div(self):
        self.assertEqual(basic.div(4, 3), 1.333, "Error - should be 1.333")
        return None

if __name__ == "__main__":
    ut.main()