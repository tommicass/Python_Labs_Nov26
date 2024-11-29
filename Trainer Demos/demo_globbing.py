#! /usr/bin/env python3
# Author: DCameron
# Description: This script willl demo howto ITERATE through files
# and the file system using an ITERATOR for loop plus the glob module.
import sys
import glob
import os

if sys.platform == "win32":
    if os.environ["HOMEPATH"]:
        home = os.environ["HOMEPATH"]
    else:
        home = r"c:\users\donal"
    pattern = home + "\*"
else:
    home = os.environ["HOME"]
    pattern = home + "/*"

print(pattern)
for file in glob.glob(pattern):
    if os.path.isfile(file):
        print(file, os.path.getsize(file))