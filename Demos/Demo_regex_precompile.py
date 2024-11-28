import re

# Open file handle for reading in text mode

fh_in = open(r"C:\Users\tcassidy\Project\Python_Labs_Nov26\labs\words", mode="rt")

# Iterate through the file handle in text mode

reobj = re.compile(r"^(.)(.).\2\1$") # Precomile pattern only once
for line in fh_in:
    #m = re.search(r"^(.)(.).\2\1$", line)
    m = reobj.search(line) # Use precompiled object, faster performance
    if m:
        print(f"Match {m.group()} on {line.rstrip()}, at {m.start()}-{m.end()}")