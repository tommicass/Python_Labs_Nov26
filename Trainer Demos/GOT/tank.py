#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This module describes a Class of Tank for an online game
"""
  Tank Class
"""

class Tank:
    # Class has Attributes/Data + Behaviour/Methods
    def __init__(self, country, model) -> None:
        self.country = country
        self.model = model
        self._speed = 0
        self._direction = 0
        self._location = {'x':0, 'y':0, 'z':0}
        self._shells = 20
        self._health = 100
        # No explicit return as called IMPLICTLY/auto

    def accel(self, increase):
        self._speed += increase
        return None
    
    def decel(self, decrease):
        self._speed -= decrease
        return None
    
    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None
    
    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None
    
    def shoot(self):
        self._shells -= 1
        return None
    
    def take_damage(self, damage):
        self._health -= damage
        return None