#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO create, grow, and shrink and access
# keys and values in a dictionary (Unordered collection with unique keys)
# Py3.6 onwards, keys are INSERTION order!
"""
  Docstring
"""
import pprint

# Create a multi-dimensional dict of lists
movies = { 'chris': ['die hard', 'trainspotting', 'barbie'],
           'tom': ['12 strong', 'forest gump', 'the matrix'],
           'andrius': ['gladiator', 'the boondock saints', 'con air'],
           'winson': ['top gun', 'terminator', 'pretty woman']
}

# Grow a dict
movies['donald'] = ['seven samurai', 'battle royale', 'the last samurai']

# Access a dict
print(f"Chris's favourite movies are {movies['chris']}")
print(f"Tom's ultimate movies is {movies['tom'][0]}")
print(f"Andrius's best films are {movies.get('andrius')}")

# Shrink a dict..
films = movies.copy() # Shallow Copy dict
films.clear() # Empty dict
movies.pop('winson') # Pop/remove 'winson' key_value.
movies.popitem() # Removes LAST INSERTED key+value
pprint.pprint(movies) # Display SORTED keys+Values in human pretty format

print("-" * 60)
# Accessing a dict and it's keys and values.
# 1.Using an ITERATOR loop plus the keys() method.
for name in movies.keys():
    print(f"{name} likes {movies[name]}")

print("-" * 60)
# 2.Using an ITERATOR loop plus the values() method.
for films in movies.values():
    print(f"Good films = {films}")

print("-" * 60)
# 3.Using an ITERATOR keys+values using items() method.
for (name, films) in movies.items():
    print(f"{name} loves the films {films}")