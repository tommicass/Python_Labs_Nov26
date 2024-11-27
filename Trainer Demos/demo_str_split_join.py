#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWWTO split and rejoin a string.
"""
  Docstring
"""
import sys

# Sample line from /etc/passwd on Linux for the root user account
line = r"root:x:0:0:The Super User:/root:/bin/ksh"

# ..and I want to modify parts of the str! IMMUTABLE!
fields = line.split(":") # Returns a LIST which is MUTABLE!
fields[4] = "The Administrator"
fields[6] = "/bin/bash"

line = ":".join(fields)  # Return a new STR
print(line)



sys.exit(0)