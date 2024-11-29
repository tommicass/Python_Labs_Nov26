#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This script will demo copy and optionally filter collections using loops, conditions and expressions, the filter() built in function, lambda function and comprehensions
"""
Script to filter collections
"""

students = ['Winson', 'Naoki', 'Tom', 'Chris', 'Andrius', 'Narla', 'Aron', 'Bobbin', 'Grace', 'Chris']

# Iterate through the source list, copy, and optionally filter using:
# 1. An iterator for loop plus source collection, optional if statement, and an expression

names = []
for name in students: # 1. Iterator loop + source
    if len(name) <= 5: # 2. Filtering condition
        names.append(name.upper()) # 3. Expression

print("-" * 60)
print(f"1. Short name = {names}")
print("-" * 60)


# 2. Using an iterator for loop plus source collection
def filter_names(name):
    """ Return true if all conditions are met """
    if len(name) <= 3:
        return True
    else:
        return False
    
names = []
for name in students: # 1. Iterator loop + source
    if filter_names(name): # 2. Filtering condition
        names.append(name.title()) # 3. Expression

print(f"2. Short name = {names}")
print("-" * 60)

# 3. Using the built in filter function plus source collection
names = list(filter(filter_names, students)) # Filter function expectes a function object - function followed by input
print(f"3. Short name = {names}")
print("-" * 60)

    # 3.1 Using a lambda function
names = list(filter(lambda name:len(name) <= 7, students)) # Or can provide a lambda function
print(f"4. Short name = {names}")
print("-" * 60)

# 4. Using list comprehension = expression, iterator loop+collection, if condition for filtering
names = [name.lower() for name in students if len(name) <= 4] # Square brackets to generate a list as output
print(f"5. Short name = {names}")
print("-" * 60)

# 5. Add tuple as output
names = [(name.upper(), len(name)) for name in students if len(name) <= 4]
print(f"6.1. Short name = {names}")
print("-" * 60)

# Change to dictionary - note use of curly brackets - also removes duplicate keys as dictionary must have unique keys
names = {name.upper(): len(name) for name in students if len(name) <= 6}
print(f"6.2. Short name = {names}")
print("-" * 60)

# Set comprehension - also removes duplicates
names = {name.upper() for name in students if len(name) <= 6}
print(f"6.3. Short name = {names}")
print("-" * 60)

# Sorted set
names = sorted({name.upper() for name in students if len(name) <= 6})
print(f"6.4. Short name = {names}")
print("-" * 60)