import re

def search_pattern(pattern, file):
    lines = 0
    with open(file, mode="rt") as fh_in:
        for line in fh_in:
            m = re.search(pattern, line)
            if m:
                lines += 1
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()},")

    return lines

num_lines = search_pattern(r"^.{19}", r"C:\Users\tcassidy\Project\Python_Labs_Nov26\labs\words")
print(f"Number of lines matched = {num_lines}")