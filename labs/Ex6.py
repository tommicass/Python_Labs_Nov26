#! /usr/bin/python
# Exercise 6, string formatting and regular expressions.
import re

infile = open(r'C:\Users\tcassidy\Project\Python_Labs_Nov26\labs\postcodes.txt', 'r')

# Variables for counting valid and invalid codes (part b)
valid = 0
invalid = 0

for postcode in infile:
    # The variable 'postcode' contain the line read from the file.
    
    # Ignore empty lines.
    if postcode.isspace(): continue
    
    # TODO (a): Remove newlines, tabs and spaces.
    postcode = re.sub(r"\s", r"", postcode) # \s does all whitespace - can also use | as an or statement 

    # TODO (a): Convert to uppercase.
    postcode = postcode.upper()

    # TODO (a): Insert a space before the final digit and 2 letters.
    #postcode = postcode[:-3] + " " + postcode[-3:]
    postcode = re.sub(r"(...)$", r" \1", postcode)
    
    # Print the reformatted postcode.
    #print (postcode)

    # TODO (b) Validate the postcode, returning a match object 'm'.
    m = 0   # TODO (b) Replace this line with a call to re.match().
    #m = re.match(r"^[A-Z]?[A-Z]?[0-9]?[A-Z]?[0-9]?\s[0-9][A-Z][A-Z]$", postcode)
    m = re.match(r"^[A-Z]{1,2}\d{1,2}[A-Z]?\s[0-9][A-Z]{2}$", postcode) # \d can be used instead of [0-9] - can also use ? or {0,1}

    if m:
        valid = valid + 1
        valid_count = "Valid"
    else:
        invalid = invalid + 1
        valid_count = "Invalid"

    print(f"{postcode} - {valid_count}")

print(f"Valid = {valid}")
print(f"Invalid = {invalid}")

infile.close()

# TODO (b) Print the valid and invalid totals.

