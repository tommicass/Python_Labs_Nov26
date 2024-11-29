#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO COPY and optionally FILTER collections
# using loops+conditions+expressions, the filter() built-in function, lambda functions
# and comprehensions.
"""
  Docstring
"""

students = ['winson', 'naoki', 'tom', 'chris', 'andrius', 'narla', 'aron', 'bobbin', 'grace', 'chris']

# ITERATE through the Source list and Copy and optionally Filter..
# 1.Using an ITERATOR for loop+collection, optional if (filtering), an expression.
wee_names = []
for name in students: # 1.Iterator Loop + source
    if len(name) <= 5: # 2.Optional condition (filtering)
        wee_names.append(name.upper()) # 3.Expression
print(f"1.Short names =", wee_names)

# 2.Using an ITERATOR for loop+collection, user function (filtering), an epression.
def filter_names(name):
    """ Return True if name is less than 6 chars """
    if len(name) <= 5:
        return True
    else:
        return False
    
wee_names = []
for name in students: # 1.Iterator Loop + source
    if filter_names(name): # 2.Optional condition (filtering)
        wee_names.append(name.upper()) # 3.Expression
print(f"2.Short names =", wee_names)

# 3.Using built-in filter() function+collection, user function (filtering).
wee_names = list(filter(filter_names, students))
print(f"3.Short names = {wee_names}")

# 4.Using built-in filter() function+collection, lambda function (filtering).
wee_names = list(filter(lambda name:len(name) <= 5, students))
print(f"4.Short names = {wee_names}")

# 5.Using LIST COMPREHENSION = expression, ITERATOR loop+collection, if condition (filtering).
wee_names = [ name.upper() for name in students if len(name) <= 5 ]
print(f"5.Short names = {wee_names}")

# 5.1.Using LIST COMPREHENSION = expression, ITERATOR loop+collection, if condition (filtering).
wee_names = [ (name.upper(), len(name)) for name in students if len(name) <= 5 ]
print(f"5.1 Short names = {wee_names}")

# 5.2.Using DICT COMPREHENSION = expression, ITERATOR loop+collection, if condition (filtering).
# EXTRA FILTERING - Duplicate Keys have been removed!
wee_names = { name.upper(): len(name) for name in students if len(name) <= 5 }
print(f"5.2 Short names = {wee_names}")

# 5.3.Using SET COMPREHENSION = expression, ITERATOR loop+collection, if condition (filtering).
# EXTRA FILTERING - Duplicate VALUES have been removed!
wee_names = { name.upper() for name in students if len(name) <= 5 }
# wee_names = sorted({ name.upper() for name in students if len(name) <= 5 })
print(f"5.3 Short names = {wee_names}")

