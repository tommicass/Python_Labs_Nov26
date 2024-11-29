#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This module describes a Class of Tank for an online game
"""
  Tank Class
"""
import vehicle

class Tank(vehicle.Vehicle):
    # Class has Attributes/Data + Behaviour/Methods
    def __init__(self, country, model) -> None:
        # Constructor - used to INITILIASE NEW objects!
        super(vehicle.Vehicle).__init__(self, country, model)
        self._direction = 0
        self._location = {'x':0, 'y':0, 'z':0}
        self._shells = 20
        self._health = 100
        # No explicit return as called IMPLICTLY/auto

    
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
    
    def __del__(self):
        # Destructor
        print("Boom..Boom")
        return None
    
    # And now for SOME SPECIAL METHODS..
    # Example of OPERATOR overloading.
    def __add__(self, other):
        return self._health + other._health
    
    # Getter Method
    def get_health(self):
        return self._health
    
    # Setter Method
    def set_health(self, newhealth):
        self._health = newhealth
        return None

    # Wrap ONE variable name interface to the two methods!
    # tank_health = property(get_health, set_health)

    # OR we could use DECORATORS to WRAP each method with another
    # function name!
    @property
    def tank_health(self):
        return self._health
    
    # Setter Method
    @tank_health.setter
    def tank_health(self, newhealth):
        self._health = newhealth
        return None



    # Example of DUCK TYPING, our Tank can now QUACK like a str!
    def __str__(self):
        return f"Model={self.model}, health={self._health}, speed={self._speed}"