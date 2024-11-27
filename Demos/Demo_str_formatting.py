#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This script will demo hwo to format strings in several ways using string concatenation, 
# escape charts, str justification methods, the str format() method and f-strings
           
           
planets = {'Mercury': 57.91, 
           'Venus': 108.2, 
           'Earth': 149.597870, 
           'Mars': 227.94
           }

# Worst case for formatting strings - string concatenation
for planet in planets.keys():
    print("\t\t" + planet + ": " + str(planets[planet]) + " Gm " + str(hex(0xff)))

# Can use * to print a string multiple times
print("-" * 60)

# Use string justification
for planet in planets.keys():
    print(planet.rjust(12) + ": " + str(planets[planet]).rjust(12) + " Gm " + str(hex(0xff)).rjust(6))

print("-" * 60)

# Use string format method
for planet in planets.keys():
    print("{0:>12s}: {1:.^12.2f} Gm {2:>#6x}".format(planet, planets[planet], 0xff))

print("-" * 60)

# Use f-strings - best method
# f is used as prefix for string to tell Python to evaluate the contents of the string
for planet in planets.keys():
    print(f"{planet:>12s}: {planets[planet]:.^12.2f} Gm {0xff:>#6x}")