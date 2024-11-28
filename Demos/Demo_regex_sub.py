#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This script will demo how to match and substitute regex patterns using the re.sub() and re.subn() functions
"""
Docstring
"""
import re

# Sample line form /etc/passwd on Linux for the root user account
line = r"root:x:0:0:The Super User:/root:/bin/ksh"

# Need to make changes, but strings are immutable (can't be edited)
new_line = re.sub(r"[sS]uper [uU]ser", r"Adminstrator", line)
new_line2 = re.sub(r"ksh$", r"bash", new_line)

print("-"*60)

print(line)
print(new_line)
print(new_line2)

print("-"*60)

(new_line, num) = re.subn(r"[sS]uper [uU]ser", r"Adminstrator", line) # subn will show how many changes have been made
(new_line2, num2) = re.subn(r"ksh$", r"bash", new_line)

print(f"{line}")
print(f"{new_line} with {num} changes")
print(f"{new_line2} with {num2} changes")

print("-"*60)