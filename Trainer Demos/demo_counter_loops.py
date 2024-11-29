#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo how to repeat a block of
# commands a specific number of times using a COUNTER loop.

count = 0 # 1. Initialise counter
while count < 10: # 2. Test Counter
    print(count)
    count += 1 # 3. Increment counter

# Alternatively we could repeat block commands using a
# for loop and the built in range(start, stop, step) function.
for num in range(0, 10, 1):
    print(num)

# for loop and the built in range(start, stop, step=1) function.
for num in range(0, 10):
    print(num)

# for loop and the built in range(start=0, stop, step=1) function.
for num in range(10):
    print(num)