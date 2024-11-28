#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO PRESERVE ONE Python object
# to a pickle file using the pickle module
"""
  Docstring
"""
import pickle
import pprint
import gzip # Other compression modules including bz2, tarfile, shutil..

movies = { 'chris': ['die hard', 'trainspotting', 'barbie'],
           'tom': ['12 strong', 'forest gump', 'the matrix'],
           'andrius': ['gladiator', 'the boondock saints', 'con air'],
           'winson': ['top gun', 'terminator', 'pretty woman']
}

# Open file handle for WRITING in BINARY mode.
# with open(r"C:\Users\Donal\Project\Python_Labs_Nov26\Trainer Demos\movies.p", mode="wb") as fh_out:
with gzip.open(r"C:\Users\Donal\Project\Python_Labs_Nov26\Trainer Demos\movies.pgz", mode="wb") as fh_out:
    # pickle.dump(movies, fh_out, protocol=5) # Pickle Protocol (0=ASCII, 1-5=BINARY)
    # pickle.dump(movies, fh_out, pickle.DEFAULT_PROTOCOL) # Default Protocol = 4
    pickle.dump(movies, fh_out, pickle.HIGHEST_PROTOCOL) # Highest Protocol = 5


# Open file handle for READING in BINARY mode.
# with open(r"C:\Users\Donal\Project\Python_Labs_Nov26\Trainer Demos\movies.p", mode="rb") as fh_in:
with gzip.open(r"C:\Users\Donal\Project\Python_Labs_Nov26\Trainer Demos\movies.pgz", mode="rb") as fh_in:
    films = pickle.load(fh_in)


pprint.pprint(movies)
print("-" * 60)
pprint.pprint(films)