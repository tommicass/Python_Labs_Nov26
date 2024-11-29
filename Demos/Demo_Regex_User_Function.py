import re
import sys

def search_pattern(pattern=r"^.{19}", file=r"C:\Users\tcassidy\Project\Python_Labs_Nov26\labs\words"):
    lines = 0
    try:
        fh_in = open(file, mode="rt")
    except FileNotFoundError as err:
        print(f"Error = {err.args[0]}, Reason = {err.args[1]}, file = {err.filename}", file=sys.stderr)
        sys.exit(1)
    except PermissionError as err:
        print(f"Error = {err.args[0]}, Reason = {err.args[1]}, file = {err.filename}", file=sys.stderr)
        sys.exit(2)
    except BaseException as err:
        print("Some other error has occurred - please investigate")
        sys.exit(3)
    else:
        for line in fh_in:
            m = re.search(pattern, line)
            if m:
                lines += 1
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()},")
        fh_in.close()
    finally:
        print("And now for something completely different...")

    return lines

#num_lines = search_pattern(r"^.{19}", r"C:\Users\tcassidy\Project\Python_Labs_Nov26\labs\words")
#print(f"Number of lines matched = {num_lines}")

def main():
    num_lines = search_pattern()
    print(f"Matched {num_lines} lines")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)