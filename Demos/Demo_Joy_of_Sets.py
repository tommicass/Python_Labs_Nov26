#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This script will demo how to create, grow, shrink, and combine sets using set operators
"""
Docstring
"""
import sys

marvel_fans = {'donald', 'naoki', 'chris', 'isla', 'grace'}
dc_fans = set() # To create an empty set - if left blank it will create empty dictionary

# Grow a set
dc_fans.add('donald')
dc_fans.add('tom')
dc_fans.add('andrius')

print("-" * 60)

# Shrink a set
#dc_fans.pop() # randomly remove an item from the set (sets have no order)
comic_fans = dc_fans.copy() # Copy set
comic_fans.clear()

print(f"Fans of marvel = {marvel_fans}")
print(f"Fans of DC = {dc_fans}")

print("-" * 60)

# Combine sets using set methods (remember venn diagrams)
print(f"Fans of EITHER marvel or DC = {marvel_fans.union(dc_fans)}")
print(f"Fans of BOTH marvel and DC = {marvel_fans.intersection(dc_fans)}")
print(f"Fans of ONLY marvel = {marvel_fans.difference(dc_fans)}")
print(f"Fans of marvel OR DC = {marvel_fans.symmetric_difference(dc_fans)}")

print("-" * 60)
# Can also use set operator characters
print(f"Fans of EITHER marvel or DC = {marvel_fans | dc_fans}")
print(f"Fans of BOTH marvel and DC = {marvel_fans & dc_fans}")
print(f"Fans of ONLY marvel = {marvel_fans - dc_fans}")
print(f"Fans of marvel OR DC = {marvel_fans ^ dc_fans}")

sys.exit(0)