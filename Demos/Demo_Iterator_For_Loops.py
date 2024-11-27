#! usr/bin/env python3
#Author: T. Cassidy
#Version: 1.0
#Description: (str/tuple/list/dict/set) using an iterator for loop

#              0           1          2        3          4
heroes = ['iron man', 'deadpool', 'batman', 'hulk', 'wonder woman']

#Iterate through the heroes list using an iterator loops

for hero in heroes:
    print(hero, end=", ")
print()

#Iterator through the list and modify the values using an iterator loop plus an index counter 

idx = 0

for hero in heroes:
    print(hero.upper(), end="\n")
    heroes[idx] = hero.upper()
    idx += 1

# Add numerate function to remove index counter

for (idx, hero) in enumerate(heroes, start=0):
    print(hero.title(), end="\n")
    heroes[idx] = hero.upper()
print("Heroes=",heroes)
