#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This script will demo a variadic function to execute a regex command
"""
App to search for regex patterns in text files
"""

import re

# Example of a variadic function that allows a variable number of parameters
def search_pattern(pattern, *files):
    """ Search for regex pattern in multiple files and return number of lines matched """
    lines = 0
    for file in files:
        with open(file, mode="rt") as fh_in:
            for line in fh_in:
                m = re.search(pattern, line)
                if m:
                    lines += 1
                    print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()},")

    return lines

num_lines = search_pattern(r"^.{20}$", 
                           r"C:\Users\tcassidy\Project\Python_Labs_Nov26\Demos\words", 
                           r"C:\Users\tcassidy\Project\Python_Labs_Nov26\Demos\words copy", 
                           r"C:\Users\tcassidy\Project\Python_Labs_Nov26\Demos\words copy 2"
                           )
print(f"Number of lines matched = {num_lines}")