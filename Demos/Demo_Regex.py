#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This script will demo how to match text data using string testing and regular expressions (regex) and the re module
"""
Docstring
"""
import re

# Open the file for reading in text mode (hence rt)
# fh = file handler object
fh_in = open(r"C:\Users\tcassidy\Project\Python_Labs_Nov26\labs\words", mode="rt")

# Iterate through the file handle one line at a time
for line in fh_in:
    # Example of string testing
    #if line.startswith("Y") and line.endswith("n\n"): # Have to add \n as each line technically ends with a new line character
    #if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line: # Remove any new line characters and then check the end line for the character
    
    # Regex Example:
    # ^ character means 'startswith'
    #m = re.search("^town", line)
     
    # $ means ends with
    #m = re.search(r"town$", line) # r is used to convert to raw string to prevent the contents being evaluated

    #m = re.search(r"^.ing$", line) # match lines with only either 1 character followed by ing
    #m = re.search(r"^[adrp]ing$", line) # match lines with only either [adrp] followed by ing
    #m = re.search(r"^...................$", line) # match lines with only 19 characters
    #m = re.search(r"[aeiou][aeiou][aeiou][aeiou]", line) # match lines with 4 consecutive vowels
    #m = re.search(r"[0-9][0-9]", line) # match lines with 2 consecutive digits
    #m = re.search(r"\.", line) # can use either \ or [] as escape characters if the desired search character is a wildcard

    #m = re.search(r"^[A-Z].*[A-Z]$", line) # match line that start and end with a capital letter, with any number of characters in between
    #m = re.search(r"^.{28}$", line) # match only words with 28 characters
    #m = re.search(r"[aeiou]{5}", line) # match only words with 5 consecutive vowels
    #m = re.search(r"^[A-Z].{3}[A-Z]$", line) # match 5 letter words that start and end with a capital letter

    m = re.search(r"^(.)(.).\2\1$", line, flags=re.IGNORECASE) # match a 5 letter palindrome + ignore case
    #m = re.search(r"^([A-Z]).*\1$", line) # match a word where the 1st letter and last letter are the same and capitalised
    #m = re.match(r"([A-Z]).*\1$", line) # .match is similar .search, but automatically starts with the pattern
    #m = re.fullmatch(r"([A-Z]).*\1\n$", line) # full match will also include hidden characters, so need to account for new line character

    if m:
        #print(line, end = "")
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()},"
              f" Groupings={m.groups()}, Group 1={m.group(1)}, Group 2={m.group(2)}")

fh_in.close()

