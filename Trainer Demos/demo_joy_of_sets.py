#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO create, and grow, and shrink and 
# combine sets using SET operators (Remember VENN diagrams from School)
"""
  Docstring
"""
marvel_fans = {'donald', 'naoki', 'chris', 'isla', 'grace'}
dc_fans = set() # Create an EMPTY SET!

# Grow a SET..
dc_fans.add('donald')
dc_fans.add('tom')
dc_fans.add('andrius')

# Change a set..
# dc_fans.pop() # Randomly remove a value.
comic_fans = dc_fans.copy() # Copy set
comic_fans.clear() # Empty the set

print(f"Fans of Marvel = {marvel_fans}")
print(f"Fans of DC = {dc_fans}")

print("-" * 60)
# COMBINE sets using SET METHODS (Remember VENN diagrams)
print(f"Fans of EITHER Marvel OR DC = {marvel_fans.union(dc_fans)}")
print(f"Fans of BOTH Marvel AND DC = {marvel_fans.intersection(dc_fans)}")
print(f"Fans of ONLY Marvel = {marvel_fans.difference(dc_fans)}")
print(f"Fans of ONLY Marvel OR DC = {marvel_fans.symmetric_difference(dc_fans)}")

print("-" * 60)
# COMBINE sets using SET OPERATORS (Remember VENN diagrams)
print(f"Fans of EITHER Marvel OR DC = {marvel_fans | dc_fans}")
print(f"Fans of BOTH Marvel AND DC = {marvel_fans & dc_fans}")
print(f"Fans of ONLY Marvel = {marvel_fans - dc_fans}")
print(f"Fans of ONLY Marvel OR DC = {marvel_fans ^ dc_fans}")

