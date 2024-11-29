#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will display the unused ports in the SERVICES file.
"""
  Docstring
"""
import sys
import re

if sys.platform == "win32":
    file = r"c:\windows\system32\drivers\etc\services"
else:
    file = r"/etc/services"

all_ports = set(range(1, 201))
used_ports = set()

with open(file, mode="rt") as fh_in:
    for line in fh_in:
        m = re.search(r"(\d+)/(udp|tcp)", line)
        if m:
            port = int(m.group(1))
            if port <= 200:
                used_ports.add(port)

print(f"All ports = {all_ports}")
print(f"Used ports = {used_ports}")
print(f"Unused ports = {all_ports - used_ports}")