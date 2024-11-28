#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This script will demo a safer way of managing file handles using a context resource manager (with statements), simulating block scope in other languages
"""
Docstring
"""

movies = {'Chris': ['Die Hard','Trainspotting','Barbie'], 
          'Tom': ['12 Strong','Forrest Gump','The Matrix'], 
          'Andrius': ['Gladiator','The Boondock Saints','Con Air'], 
          'Winson': ['Top Gun','Terminator','Pretty Woman'], 
          }

# Open filehandle for writing in text mode
with open(r"C:\Users\tcassidy\Project\Python_Labs_Nov26\Demos\movies.txt", mode = "wt") as fh_out:
    for name in movies.keys():
        #print(name, movies[name], file=fh_out) # can use print function to write to files
        fh_out.write(f"{name} : {movies[name]}\n")

        #don't need to close file handlers - with statement auto closes the file handler after use

print("-"*60)

# Open filehandle for reading in text mode
with open(r"C:\Users\tcassidy\Project\Python_Labs_Nov26\Demos\movies.txt", mode = "rt") as fh_in:
    for line in fh_in:
        print(line, end="")