#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo howto ITERATE through a
# SEQUENCE (str/tuple/list/dict/set) using an ITERATOR for loop.

#             0            1         2         3           4
heroes = ['iron man', 'deadpool', 'batman', 'hulk', 'wonder woman']

# ITERATE through the heroes LIST using an ITERATOR loop..
for hero in heroes:
    print(hero, end="\n")

# ITERATE through the LIst and MODIFY the values using an
# ITERATOR loop plus an index counter.
idx = 0
for hero in heroes:
    print(hero.upper())
    heroes[idx] = hero.upper()
    idx += 1
print("Heroes=", heroes)

# ITERATE through the List and MODIFY the values using an
# ITERATOR loop plus built-in enumerate() function
for (idx, hero) in enumerate(heroes, start=0):
    print(hero.title())
    heroes[idx] = hero.title()
print("Heroes=", heroes)