#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will display the valid postcodes in the postcodes.txt file.
"""
  Docstring
"""
import re

fh_in = open(r"C:\Users\Donal\Project\Python_Labs_Nov26\labs\postcodes.txt", mode="rt")

valid = 0
invalid = 0

for postcode in fh_in:
    # Ques 1 Solutions..
    if postcode.isspace(): continue
    postcode = postcode.upper()
    postcode = re.sub(r"\s+", r"", postcode)
    postcode = re.sub(r"(\d[A-Z]{2})$", r" \1", postcode)
    
    # Ques 2 Solutions..
    m = re.search(r"^[A-Z]{1,2}\d{1,2}[A-Z]?\s\d[A-Z]{2}$", postcode)
    if m:
        valid += 1
        print(postcode)
    else:
        invalid += 1

fh_in.close()
print(f"Valid postcodes = {valid}")
print(f"Invalid postcodes = {invalid}")