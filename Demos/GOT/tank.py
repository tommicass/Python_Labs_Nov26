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
        # Constructor
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
    
    def __del__(self):
        # Destructor
        print("Boom..Boom")
        return None
    
    # and now for some special methods:
    # Example of operator overloading

    def __add__(self, other):
        return self._health + other._health
    
    # Getter method
    def get_health(self):
        return self._health
    
    # Setter method
    def set_health(self, newhealth):
        self._health = newhealth
        return None
    
    # Wrap one variable interface to the 2 methods (getter 1st, then setter)
    tank_health = property(get_health, set_health)
    # Or could use decorators:
    @property
    def tank_health(self):
        return self._health
    @tank_health.setter
    def tank_health(self, newhealth):
        self._health = newhealth
        return None

    # Example of duck typing, our tank can now quack like a strs
    def __str__(self):
        return f"Model={self.model}, Health={self._health}%, Speed={self._speed}kph"