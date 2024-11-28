#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This script will demo how to open, close, read and write randomly to a file using the .seek() and .tell() methods
"""
Docstring
"""
import sys

SOF = 0 # Start of file
CUR = 1 # Current file position
EOF = 2 # End of file

# Open filehandle for reading  in text mode
with open(r"C:\Users\tcassidy\Project\Python_Labs_Nov26\Demos\movies.txt", mode = "rt") as fh_in:
    fh_in.seek(90, SOF) # Seek forwards 90 characters from start of file
    text = fh_in.read(30)
    print(f"Text at position {fh_in.tell() - len(text)} = {text}")

print("-"*60)

# Open filehandle for reading  in text mode
with open(r"C:\Users\tcassidy\Project\Python_Labs_Nov26\Demos\movies.txt", mode = "rb") as fh_data:
    fh_data.seek(90, SOF) # Seek forwards 90 bytes from start of file
    text = fh_data.read(30)
    print(f"Text at position {fh_data.tell() - len(text)} = {text}")

    fh_data.seek(-90, EOF) # 2 indicates backwards direction
    text = fh_data.read(30)
    print(f"Text at position {fh_data.tell() - len(text)} = {text}")

print("-"*60)