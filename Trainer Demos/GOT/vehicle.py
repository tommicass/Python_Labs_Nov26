#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo
"""
  BASE Class of Vehicle for Tanks, Jeeps and Trucks
"""
class Vehicle:
    def __init__(self, country, model) -> None:
        self.country = country
        self.model = model
        self._speed = 0

    def accel(self, increase):
        self._speed += increase
        return None
    
    def decel(self, decrease):
        self._speed -= decrease
        return None