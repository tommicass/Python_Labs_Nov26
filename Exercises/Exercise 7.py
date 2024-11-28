import re

all_ports = set(range(1,201))
used_ports = set()

with open(r"C:\Users\tcassidy\Project\Python_Labs_Nov26\Exercises\services", mode="rt") as fh_in:
    for line in fh_in:
        m = re.search(r"(\d+)/(tcp|udp)", line)
        if m:
            port = int(m.group(1))
            if port <= 200:
                used_ports.add(port)

unused_ports = all_ports - used_ports
print(unused_ports)