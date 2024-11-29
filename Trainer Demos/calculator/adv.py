#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This Modue defines advanced functions for a calculator app
"""
  Advanced functions for Calculator App including modulus, power and sqrt
"""

def mod(x, z):
    """ Return REMAINDER of x modulus z """
    return  x % z

def power(x, z):
    """ Return the power of x to z as a float """
    return float(x**z)

def sqrt(x):
    """ Return square root of x to 2 decimal places """
    return round(x**0.5, 2)
