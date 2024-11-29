#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This module defines a collection of calculator functions
"""
Basic calculator functions including add, sub, mul and div functions
"""
import sys

def add(*args):
    """ Return SUM of all arguments """
    total = 0
    for num in args:
        total += num
    return total

def sub(x, z):
    """ Return result of x subtract z """
    return x - z

def mul(*args):
    """ Return product of all the arguments """
    total = 1
    for num in args:
        total *= num
    return total

def div(x, z):
    """ Return divisor of x divided by z to 3 decimal places """
    return round(x/z, 3)

sys.exit(0)