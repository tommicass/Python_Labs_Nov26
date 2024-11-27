#! usr/bin/env python3
#Author: T. Cassidy
#Version: 1.0
#Description: Generate 6 random unique lottery numbers

import random

lotto = []
count = 0

while len(lotto) < 6:
    num = random.randint(1,50)
    count += 1

    if num not in lotto:
        lotto.append(num)
    else:
        print("Duplicate number = " + str(num))

lotto.sort()

print(lotto)
print(count)

#Version: 1.1 - Using sets
# Sets can't have duplicates, so no need to check for duplicates 

lotto = set()

while len(lotto) < 6:
    num = random.randint(1,50)
    lotto.add(num)

print(f"Lottery Numbers are {sorted(lotto)}")
