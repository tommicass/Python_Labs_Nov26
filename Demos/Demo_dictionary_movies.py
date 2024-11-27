#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This script will demo how to create, grow, shrink and access keys and values in a dictionary with unique keys
"""
Docstring
"""
import sys
import pprint # Pretty Print

movies = {'Chris': ['Die Hard','Trainspotting','Barbie'], 
          'Tom': ['12 Strong','Forrest Gump','The Matrix'], 
          'Andrius': ['Gladiator','The Boondock Saints','Con Air'], 
          'Winson': ['Top Gun','Terminator','Pretty Woman'], 
          }

# Grow a dictionary - add entries

movies['Naoki'] = ['Titanic', 'Star Wars', 'Spiderman']
movies['Donald'] = ['Seven Samuraii', 'Battle Royale', 'The Last Samuraii']

# Print 'Die Hard'
print(movies['Chris'][0])

# Print 'e' character
print(movies['Chris'][0][2])

print(f"Chris' favourite movies are {movies['Chris']}")
print(f"Tom's ultimate favourite movie is {movies['Tom'][0]}")
print(f"Andrius' best film is {movies.get('Andrius')[0]}")

# Shrink a dictionary

films = movies.copy() # Shallow copy the dictionary
films.clear() # Empty the dictionary

movies.pop('Winson')
movies.popitem() # Remove most recently added item
pprint.pprint(movies)

# Accessing a dictionary's values and keys
# 1. Using an iterator loop plus the keys() method

for names in movies.keys():
    for n in range(3):
        print(f"{names} likes {movies[names][n]}")

# 2. Using an iterator loop plus the values() method

for films in movies.values():
    print(f"Good films = {films}")

# 3. Using an iterator loop through keys+values using the items() method

for (name, films) in movies.items():
    print(f"{name} loves the films {films}")

sys.exit(0)