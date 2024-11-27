#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This script will demo
"""
Docstring
"""
import sys

for pos in range(0, 65536):
    try:
        print(chr(pos), end=" ")
        if pos % 16 == 0:
            print("")
    except UnicodeEncodeError:
        print("")

sys.exit(0)
