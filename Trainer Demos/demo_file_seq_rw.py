#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO open, and read, write, and append, and close
# a TEXT file.
"""
  Docstring
"""
import sys
movies = { 'chris': ['die hard', 'trainspotting', 'barbie'],
           'tom': ['12 strong', 'forest gump', 'the matrix'],
           'andrius': ['gladiator', 'the boondock saints', 'con air'],
           'winson': ['top gun', 'terminator', 'pretty woman']
}

# Open file handle for WRITING in TEXT mode.
fh_out = open(r"C:\Users\Donal\Project\Python_Labs_Nov26\Trainer Demos\movies.txt", mode="wt")

# ITERATE through movies dict and WRITE movie info to file handle.
for name in movies.keys():
    print(f"{name}: {movies[name]}", end="\n", file=sys.stdout) # To Terminal..
    print(f"{name}: {movies[name]}", end="\n", file=fh_out) # To File..
    # fh_out.write(f"{name}: {movies[name]}\n")

# fh_out.flush() # Flush buffers.
fh_out.close() # Flush buffers and close file.

print("-" * 60)
# Open file handle for READING in TEXT mode.
fh_in = open(r"C:\Users\Donal\Project\Python_Labs_Nov26\Trainer Demos\movies.txt", mode="rt")

# text = fh_in.read() # Read ENTIRE file into str object. Be Careful of Huge files!
# text = fh_in.read(30) # Read NEXT 30 chars into str object.
# text = fh_in.readline() # Read NEXT line into str object.
# lines = fh_in.readlines() # Read ENTIRE file into LIST object. Be Careful of Huge files!
# print(lines[-1]) # Can INDEX list to get specific lines = useful!

# ITERATE through the file ONE line at a time!
# Using an ITERATOR lOOP plus ITERATOR object (iter/next).
for line in fh_in:
    print(line, end="")

fh_in.close()