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

print(lotto)
print(count)