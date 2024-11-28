#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO match and SUBSTITUTE regex patterns
# using the re.sub() and re.subn() functions.
"""
  Docstring
"""
import re

# Sample line from /etc/passwd on Linux for the root user account.
line = r"root:x:0:0:The Super User:/root:/bin/ksh"

# And I want to modify the line str object! IMMUTABLE!
line = re.sub(r"[sS]uper [uU]ser", r"Administrator", line) # Returns modified str.
(line, num) = re.subn(r"ksh$", r"bash", line) # Returns a TUPLE (modified str, num changes)

print(f"Modified line = {line} with {num} changes")