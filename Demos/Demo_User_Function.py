#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This script will demo user Functions

def say_hello(greeting:str, recipient:str="amichi"): # Can define defaults in function definition - if assigning default, everything afterwards must also have defaults
    message = (f"{greeting} {recipient}")
    print(message)
    return

say_hello("hello", "everyone") # example of positional parameter passing
say_hello(greeting="konichiwa", recipient="tomodachi") # example of named parameter passing
say_hello(recipient="tous mes amis", greeting="bonjour") # named parameter passing allows variables in a different order
say_hello("Ciao") # will rely on default option for recipient
say_hello("Ciao", ['Winson', 'Andrius', 'Chris'])
print("-" * 60)
print(f"Annotations for say_hello = {say_hello.__annotations__}")