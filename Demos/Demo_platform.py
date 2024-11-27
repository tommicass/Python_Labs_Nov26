#! usr/bin/env python3
#Author: T. Cassidy
#Version: 1.0
#Description: Check OS platform

import sys
import os
import platform

if sys.platform == 'win32':
    homedir = os.environ['HOMEPATH']
else:
    homedir = os.environ['HOME']

print(platform.machine())
print(platform.architecture())
print(platform.node())
print(platform.python_implementation())

print(homedir)

try:
    sys.exit(0) # Exit program with return code 0 (success) - error codes 1-255 are used for error codes
except SystemError:
    print("Quitting Program")
    sys.exit(0)