#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This script will demo how to generate a collection one object at a time using a generator function
"""
Docstring
"""

def get_numbers():
    """ Return an entire list of numbers """
    #print("Executing get_numbers...")
    numbers = []
    for x in range(0,100):
        numbers.append(x)
        #print(numbers)
    return numbers

def generate_numbers():
    """ Yield one object at a time from a collection of numbers """
    print("Executing generate_numbers...")
    for x in range(0,100):
        yield x

for z in generate_numbers():
    print(z)

# Alternatively we could use a while loop and the next function to get the next value

gen = generate_numbers()
while True:
    num = next(gen, -1) # False is default
    if num != -1:
        print(num)
    else:
        break

