#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This is an ultra realistic calculator app.
"""
  Calculator App with Basic and Advanced functions.
"""
import sys
import basic
import adv

def main():
    while True:
        menu = """
                Welcome to ShinEtsu Calc App
                ----------------------------
                1. Add
                2. Mul
                3. Div
                4. Mod
                5. Sqrt
                Q=Quit
        """

        print(menu)
        option = input("Enter option: ")
        if option.lower() == "q": break

        match option:
            case "1":
                num1 = int(input("Enter num: "))
                num2 = int(input("Enter num: "))
                print(f"{num1} + {num2} = {basic.add(num1, num2)}")
            case "2":
                num1 = int(input("Enter num: "))
                num2 = int(input("Enter num: "))
                print(f"{num1} * {num2} = {basic.mul(num1, num2)}")
            case "3":
                num1 = int(input("Enter num: "))
                num2 = int(input("Enter num: "))
                print(f"{num1} / {num2} = {basic.div(num1, num2)}")
            case "4":
                num1 = int(input("Enter num: "))
                num2 = int(input("Enter num: "))
                print(f"{num1} % {num2} = {adv.mod(num1, num2)}")
            case "5":
                num1 = int(input("Enter num: "))
                print(f"Square root of {num1} = {adv.sqrt(num1)}")
            case _:
                print("Invalid option")
    return None


# Namespace Trick
if __name__ == "__main__":
    # Execute ONLY if ran directly as a program
    # Ignore if imported as a module.
    main()
    sys.exit(0)