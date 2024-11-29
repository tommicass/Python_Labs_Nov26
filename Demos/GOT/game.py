#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This module
"""
Docstring
"""
import sys
import tank

def main():
    # Create/instantiate 3 new tank objects
    winson_tank = tank.Tank("German", "Tiger")
    andrius_tank = tank.Tank("American", "Sherman")
    chris_tank = tank.Tank("British", "Churchill")

    # And the game begins

    winson_tank.accel(64)
    chris_tank.accel(31)

    andrius_tank.rotate_left(289)
    andrius_tank.accel(27)
    andrius_tank.shoot()

    # ... and success

    winson_tank.damage(59)
    chris_tank.damage(39)

    # and now for some game visuals (print statements)

    #print(f"Winson Tank health = {winson_tank._health}%") = poor code to directly access private variables
    #print(f"Chris Tank health = {chris_tank._health}%")

    # This is an example of operator overloading
    #print(f"The health of Winson's & Chris' tank = {winson_tank + chris_tank}%")
    print(f"The health of Winson's & Chris' tank = {winson_tank.get_health() + chris_tank.get_health()}%")

    # Winson tank has received a health boost
    winson_tank.set_health(100)
    #print(f"The new health of Winson tank is {winson_tank._health}%")
    print(f"The new health of Winson's tank is {winson_tank.get_health()}%")
    print(f"The new health of Winson's tank is {winson_tank.tank_health}%") # Using property method

    print(f"Status of Winson's tank = {winson_tank}")

    return None

main()


if __name__ == "__main__":
    sys.exit(0)