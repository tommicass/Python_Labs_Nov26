#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This script will demo how to split and rejoin a string
"""
Docstring
"""
import sys

# Sample line from etc/passwd on Linux for the root user account
line = r"root:x:0:0:The Super User:/root:/bin/ksh"

fields = line.split(":") # Returns a list - list can be editted

print(fields)

# Change fields 4 + 6
fields[4] = "The Administrator"
fields[6] = "bin/bash"

print(fields)

# Join list back into a string but using : as delimiter
line = ":".join(fields)

print(line)

sys.exit(0)