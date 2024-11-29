#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO match text data using str testing
# and Regular Expressions/Regex and the re module.
"""
  Docstring
"""
import re
import sys

def search_pattern(pattern=r"^.{19}$", file=r"C:\Users\Donal\Project\Python_Labs_Nov26\labs\words"):
    lines = 0
    try:
        fh_in = open(file, mode="rt")
    except FileNotFoundError as err:
        print(f"Error={err.args[0]}, reason={err.args[1]}, file={err.filename}", file=sys.stderr)
        sys.exit(1)
    except PermissionError as err:
        print(f"Error={err.args[0]}, reason={err.args[1]}, file={err.filename}", file=sys.stderr)
        sys.exit(2)
    except BaseException as err:
        print("Some other error occurred, Investigate")
        sys.exit(3)
    else:
        for line in fh_in:
            m = re.search(pattern, line ) # Match Pattern
            if m:
                lines += 1
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
        fh_in.close()
    finally:
        print("And now for something completely different..")
    return lines

def main():
    num_lines = search_pattern()
    print(f"Matched {num_lines} lines")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)