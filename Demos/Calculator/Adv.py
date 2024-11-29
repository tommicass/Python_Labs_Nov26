#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This module defines a set of advanced calculator functions
"""
Advanced functions for calculator app including modulus, power & sqrt
"""
import sys

def mod(x, z):
    """ Return remained for x modulus z """
    return x % z

def power(x, z):
    """ Return power of x to z as a float """
    return float(x**z)

def sqrt(x):
    """ Return the square root of x as a float to 2 decimal places"""
    return round(x**0.5, 2)

if __name__ == "__main__":
    # Include standalone code to run if running as a program (not a module)
    sys.exit(0)