#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO match text data using str testing
# and Regular Expressions/Regex and the re module.
"""
  Docstring
"""
import re

# Open file handle for READING in TEXT mode
fh_in = open(r"C:\Users\Donal\Project\Python_Labs_Nov26\labs\words", mode="rt")

# Iterate through the file handle one line at a time..
for line in fh_in:
    # Example of str testing
    # if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    # m = re.search(r"town", line) # Match lines with "town" in the string.
    # m = re.search(r"^town", line) # Match lines starting with "town".
    # m = re.search(r"town$", line) # Match lines ending with "town".
    # m = re.search(r"^[A-Z]", line) # Match lines starting with CAPITAL.
    # m = re.search(r"^.ing$", line) # Match lines with ONLY one char followed by "ing".
    # m = re.search(r"^[adrp]ing$", line) # Match lines with ONLY either [adrp] followed by "ing".
    # m = re.search(r"^...................$", line) # Match lines with EXACTLY 19 chars.
    # m = re.search(r"^.{19}$", line) # Match lines with EXACTLY 19 chars.
    # m = re.search(r"[aeiou][aeiou][aeiou]", line) # Match lines with 3 consecutive vowels".
    # m = re.search(r"[aeiou]{5,}", line) # Match lines with at least 5 consecutive vowels.
    # m = re.search(r"[0-9][0-9]", line) # Match lines with 2 consecutive digits.
    # m = re.search(r"\.", line) # Match lines with a DOT. Preferred
    # m = re.search(r"[.]", line) # Match lines with a DOT.
    # m = re.search(r"^[A-Z].*[A-Z]$", line) # Match lines start/end with a CAPITAL.
    # m = re.search(r"^[A-Z].{3}[A-Z]$", line) # Match lines of 5 chars start/end with a CAPITAL.
    m = re.search(r"^(.)(.).\2\1$", line, flags=re.IGNORECASE) # Match 5 char palindromes + IGNORE CASE
    # m = re.search(r"^([A-Z]).*\1$", line) # Match lines start/end with SAME CAPITAL.
    # m = re.match(r"([A-Z]).*\1$", line) # Match AUTO lines STARTING with Pattern! Don't like THIS!
    # m = re.fullmatch(r"^([A-Z]).*\1\n$", line) # Match ENTIRE line including HIDDEN chars like newline!
    if m:
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()} ,"
              f" Groupings={m.groups()}, Group 1={m.group(1)}")

fh_in.close()