#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO define and call a VARIADIC user function.
"""
  App to search for Regex patterns in text files. READ by help() for USERS!
"""
import re

# Example of a VARIADIC function that allows variable num of parameters.
def search_pattern(pattern=r"^.{19}$", *files):
    """ Search for Regex pattern in multiple file/s and return num lines matched """
    lines = 0
    for file in files:
        with  open(file, mode="rt") as fh_in:
            for line in fh_in:
                m = re.search(pattern, line ) # Match Pattern
                if m:
                    lines += 1
                    print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
    return lines



num_lines = search_pattern(r"^.{20}$", r"C:\Users\Donal\Project\Python_Labs_Nov26\TRainer Demos\words",
                            r"C:\Users\Donal\Project\Python_Labs_Nov26\Trainer Demos\words2",
                            r"C:\Users\Donal\Project\Python_Labs_Nov26\Trainer Demos\words3")
print(f"Matched {num_lines} lines")