#! usr/bin/env python3
#Author: T. Cassidy
#Version: 1.0
#Description: This script will demo how to iterate through files in the file system using an iterator for loop plus the glob module
# glob is another name for wildcard

import glob
import os
import sys

if sys.platform == "win32":
    #print(os.environ)
    home = os.environ["USERPROFILE"]
    pattern = home + r"\*" # r is used to define file path as raw string
else:
    home = os.environ["HOME"]
    pattern = home + "/*"

for files in glob.glob(pattern):
    if os.path.isfile(files): #only print items if a file
        print(files, os.path.getsize(files))