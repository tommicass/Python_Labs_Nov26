#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This script will demo how to open, read, write, append and close a text file
"""
Docstring
"""

movies = {'Chris': ['Die Hard','Trainspotting','Barbie'], 
          'Tom': ['12 Strong','Forrest Gump','The Matrix'], 
          'Andrius': ['Gladiator','The Boondock Saints','Con Air'], 
          'Winson': ['Top Gun','Terminator','Pretty Woman'], 
          }

# Open filehandle for writing in text mode
fh_out = open(r"C:\Users\tcassidy\Project\Python_Labs_Nov26\Demos\movies.txt", mode = "wt")

# Iterate through movies dictionary and write move info to files handle
for name in movies.keys():
    print(name, movies[name])
    fh_out.write(f"{name} : {movies[name]}\n")

fh_out.close()

print("-"*60)

# Open filehandle for reading in text mode
fh_in = open(r"C:\Users\tcassidy\Project\Python_Labs_Nov26\Demos\movies.txt", mode = "rt")

#text = fh_in.read() # Reads an entire file into a string object - be careful of large files
#text = fh_in.read(30) # Reads next 30 characters into a string object
#text = fh_in.readline() # Reads next line into a string object
text = fh_in.readlines() # Reads entire file into a list object - be careful of large files 
print(text)

fh_in.close()