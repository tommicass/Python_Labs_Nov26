#! usr/bin/env python3
#Author: T. Cassidy
#Version: 1.0
#Description: Demo for repeating counter loops

count = 0 # 1. Initialise the counter

while count < 10: #  2. Test the counter
    print(count)
    count += 1 # 3. Increment the counter

for num in range(0, 10, 1): # range function uses start point, end point and step increment (default step is 1)
    print (num)

for num in range(10): # if only 1 parameter is specified, the value will be taken as the end point
    print (num)