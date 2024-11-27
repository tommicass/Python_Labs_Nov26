#! /usr/bin/env python3
# Author: DCameron
# Description: This script will simulate a high street bank PIN machine.

master_pin = "0123"
pin = None
attempts = 0

while pin != master_pin and attempts < 3:
    pin = input("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
        break
    else:
        print("Invalid PIN")
        attempts += 1
else:
    # EXECUTES only ONCE when while condition becomes False
    print("Too many attempts")
    print("Your card has been retained. Have a nice day")


print("Done.")