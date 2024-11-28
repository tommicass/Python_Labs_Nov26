#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This script will demo the pickle module
"""
Docstring
"""
import pickle
import pprint
import gzip # Other compression modules include bz2, tarfile, shutil

movies = {'Chris': ['Die Hard','Trainspotting','Barbie'], 
          'Tom': ['12 Strong','Forrest Gump','The Matrix'], 
          'Andrius': ['Gladiator','The Boondock Saints','Con Air'], 
          'Winson': ['Top Gun','Terminator','Pretty Woman'], 
          }

# Open file handle for writing in binary mode
with open(r"C:\Users\tcassidy\Project\Python_Labs_Nov26\Demos\movies.pkl", mode="wb") as fh_out:
    pickle.dump(movies, fh_out, protocol=0) # pickle protocol goes from 0=ASCII, 1-5=Binary - highest number is most efficient
    pickle.dump(movies, fh_out, pickle.DEFAULT_PROTOCOL) # Default protocol - (4)
    pickle.dump(movies, fh_out, pickle.HIGHEST_PROTOCOL) # Default to highest level protocol (5)

# Open file handle for reading in binary mode
with open(r"C:\Users\tcassidy\Project\Python_Labs_Nov26\Demos\movies.pkl", mode="rb") as fh_in:
    films = pickle.load(fh_in)
    pprint.pprint(movies)
    print("-" * 60)
    pprint.pprint(films)

print("-" * 60)

with gzip.open(r"C:\Users\tcassidy\Project\Python_Labs_Nov26\Demos\movies.pgz", mode="wb") as fh_out:
    pickle.dump(movies, fh_out, protocol=0)

with gzip.open(r"C:\Users\tcassidy\Project\Python_Labs_Nov26\Demos\movies.pgz", mode="rb") as fh_in:
    films = pickle.load(fh_in)
    pprint.pprint(movies)
    print("-" * 60)
    pprint.pprint(films)