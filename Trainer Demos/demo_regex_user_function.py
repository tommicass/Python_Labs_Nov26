#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO match text data using str testing
# and Regular Expressions/Regex and the re module.
"""
  Docstring
"""
import re

def search_pattern(pattern=r"^.{19}$", file=r"C:\Users\Donal\Project\Python_Labs_Nov26\labs\words"):
    lines = 0
    with  open(file, mode="rt") as fh_in:
        for line in fh_in:
            m = re.search(pattern, line ) # Match Pattern
            if m:
                lines += 1
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
    return lines


num_lines = search_pattern()
print(f"Matched {num_lines} lines")