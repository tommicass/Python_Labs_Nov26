#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo how to TEST which platform you
# are running on and will get the HOME path of the user.

import sys
import os
import platform

if sys.platform == "win32":
    home = os.environ["HOMEPATH"]
else:
    home = os.environ["HOME"]
                      
print("My home directory is", home)

print(platform.system())
print(platform.machine())
print(platform.architecture())
print(platform.node())
print(platform.python_implementation())

try:
    sys.exit(0) # Exit program with Return Code (0=success, 1-255=error code)
except SystemError:
    print("Quitting program..")
    sys.exit(0)