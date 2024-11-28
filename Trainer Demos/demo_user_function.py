#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO define, name, call and optionally pass
# parameters in and optionally return data from a user function.
"""
  Docstring
"""

# EXample of a User function with parameter passing
# and optional default values. And annotations (embedded
# comment specifying preferred datatype).
def say_hello(greeting:str="ciao", recipient:str="amici")->None:
    message = f"{greeting} {recipient}"
    print(message)
    return None


say_hello("hello", "my friends") # Example of Positional Parameter passing.
say_hello(greeting="konichiwa", recipient="tomodachi") # Named parameter passing.
say_hello(recipient="mes amis", greeting="bonjour") # Named parameter passing (different order)
say_hello("ciao", recipient="amici") # Mixed parameter passing (positiona->named)
say_hello("ciao", ['tom', 'naoki', 'winson'])
say_hello()

print(F"Annotations for say_hello = {say_hello.__annotations__}")