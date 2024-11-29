#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This script will demo
"""
Docstring
"""

import Basic as basic

def test_add():
    assert basic.add(4, 3) == 7, "Error - should be 7"
    assert basic.add(4, 3, 2) == 9, " Error - should be 9"
    return None

def test_mul():
    assert basic.mul(4, 3) == 12, "Error - should be 12"
    assert basic.mul(4, 3, 2) == 24, " Error - should be 24"
    return None

def test_div():
    assert basic.div(4, 3) == 1.333, "Error - should be 1.333"
    return None

def main():
    print("Starting unit tests...")

    test_add()
    test_mul()
    test_div()

    print("Unit test successful")
    return None

if __name__ == "__main__":
    main()