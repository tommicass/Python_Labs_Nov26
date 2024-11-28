#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo a SAFER way of managing file handles
# using a Context Resource Manager (with statement). Simulating BLOCK Scope.
"""
  Docstring
"""
movies = { 'chris': ['die hard', 'trainspotting', 'barbie'],
           'tom': ['12 strong', 'forest gump', 'the matrix'],
           'andrius': ['gladiator', 'the boondock saints', 'con air'],
           'winson': ['top gun', 'terminator', 'pretty woman']
}

# Open file handle for WRITING in TEXT mode.
with open(r"C:\Users\Donal\Project\Python_Labs_Nov26\Trainer Demos\movies.txt", mode="wt") as fh_out:
    for name in movies.keys():
        print(f"{name}: {movies[name]}", end="\n") # To Terminal..
        print(f"{name}: {movies[name]}", end="\n", file=fh_out) # To File..
        # End of Block, fh_out is closed and deleted automatically.


print("-" * 60)
# Open file handle for READING in TEXT mode.
with open(r"C:\Users\Donal\Project\Python_Labs_Nov26\Trainer Demos\movies.txt", mode="rt") as fh_in:
    for line in fh_in:
        print(line, end="")

