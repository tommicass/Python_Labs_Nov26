#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will generate 6 unique random lottery
# numbers
import random

"""
lotto = []

while len(lotto) < 6:
    num = random.randint(1, 50)
    if num not in lotto:
        lotto.append(num)
    else: 
        print("Duplicate number =", num)
"""

lotto = set() # PYTHONIC solution.

while len(lotto) < 6:
    num = random.randint(1, 50)
    lotto.add(num)

print("Lottery numbers =", sorted(lotto))