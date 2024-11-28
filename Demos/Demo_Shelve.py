#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This script will demo the shelve module
"""
Docstring
"""

import shelve

movies = {'Chris': ['Die Hard','Trainspotting','Barbie'], 
          'Tom': ['12 Strong','Forrest Gump','The Matrix'], 
          'Andrius': ['Gladiator','The Boondock Saints','Con Air'], 
          'Winson': ['Top Gun','Terminator','Pretty Woman'] 
          }

tv_series = {'Chris': ['Walking Dead', 'Yellow Stone'],
             'Tom': ['Breaking Bad', 'The Boys'],
             'Andrius': ['Outlander', 'Dads Army']
             }

books = {'Andrius': 'Dummys Guide to Python',
         'Winson': 'Extreme Ironing'
         }

with shelve.open(r"C:\Users\tcassidy\Project\Python_Labs_Nov26\Demos\media") as db:
    db['movies'] = movies
    db['tv series'] = tv_series
    db['books'] = books

with shelve.open(r"C:\Users\tcassidy\Project\Python_Labs_Nov26\Demos\media") as db:
    print(f"Chris' favourite moveis are {db['movies']['Chris']}")
    print(f"Tom's favourite TV Series is {db['tv series']['Tom'][1]}")
    print(f"Winson's favourite book is {db['books']['Winson']}")
