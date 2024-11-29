#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo
"""
  Docstring
"""
import sys
import tank

def main():
    # Create/Instantiate 3 new Tank objects..
    thomas_tank = tank.Tank("german", "tiger")
    chris_tank = tank.Tank("american", "sherman")
    naoki_tank = tank.Tank("british", "churchill")

    # And the game begins..
    thomas_tank.accel(64)
    chris_tank.accel(31)

    naoki_tank.rotate_left(289)
    naoki_tank.accel(27)
    naoki_tank.shoot()

    # ..and success.
    thomas_tank.take_damage(59)
    chris_tank.take_damage(39)

    # And now for some game visuals - well at least some print statements!
    # print(f"Health of Thomas the tank is {thomas_tank._health}") # POOR CODE!

    # Example of operator overloading
    print(f"Health of Thomas and Chris's Tanks = {thomas_tank + chris_tank}")

    # Thomas has received a HEALTH boost.
    # thomas_tank._health = 100 # DO NOT ACCESS PRIVATE Variables!
    # print(f"New health of Thomas's tank is {thomas_tank._health}")

    # Better to use a SETTER AND GETTER methods :-)
    thomas_tank.set_health(101)
    print(f"NEwhealth of Thomas's Tank is {thomas_tank.get_health()}")

    thomas_tank.tank_health = 102
    print(f"NEwhealth of Thomas's Tank is {thomas_tank.tank_health}")

    print(f"Status of Thomas's Tank = {thomas_tank}")

    return None

# Namepace Trick
if __name__ == "__main__":
    main()
    sys.exit(0)