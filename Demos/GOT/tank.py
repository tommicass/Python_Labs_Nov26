#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This module describes a class of tank for an online game
"""
Tank class
"""

class Tank:
    # Class has attributes/Data + Behaviours/Methods
    def __init__(self, country, model):
        self.country = country
        self.model = model
        # Underscores used to make variables 'private'
        self._speed = 0
        self._direction = 0
        self._location = {'x':0, 'y':0, 'z':0}
        self._shells = 20
        self._health = 100
        # No return as called implicitly (automatically as __init__ function)

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
    
    def damage(self, damage):
        self._health -= damage
        return None