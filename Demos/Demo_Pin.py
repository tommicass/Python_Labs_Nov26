#! usr/bin/env python3
#Author: T. Cassidy
#Version: 1.0
#Description: This script will simulate a high street bank pin machine

import getpass

master_pin = "0123"
pin = None
attempts = 0

while pin != master_pin and attempts < 3:
    pin = getpass.getpass("Enter Pin: ")
    if pin == master_pin:
        print("Valid PIN")
        break # break prevents else statement from executing - drops out of while loop
    else:
        print("Invalid PIN")
        attempts += 1
else: 
    #Executes only once when while condition becomes false
    print("Too many attempts")
    print("Card retained")

print("Done")