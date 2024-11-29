#! user/bin/env Python3
# Author: TCassidy
# Version: 1.0
# Description: This is a calculator app
"""
Calculator app with basic functions
"""
import sys

import Adv as adv
import Basic as basic

def main():
    while True:
        menu = """
                Welcome to Shin-Etsu Calc app
                -----------------------------
                1. Add
                2. Subtract
                3. Multiply
                4. Divide
                5. Mod
                6. Square Root
                Q = Quit
        """

        print(menu)
        option = input("Enter Option: ")
        if option.lower() == "q": break

        match option:
            case "1":
                num1 = int(input("Enter 1st Number"))
                num2 = int(input("Enter 2nd Number"))
                print(f"{num1} + {num2} = {basic.add(num1, num2)}")
            case "2":
                num1 = int(input("Enter 1st Number"))
                num2 = int(input("Enter 2nd Number"))
                print(f"{num1} - {num2} = {basic.sub(num1, num2)}")
            case "3":
                num1 = int(input("Enter 1st Number"))
                num2 = int(input("Enter 2nd Number"))
                print(f"{num1} x {num2} = {basic.mul(num1, num2)}")
            case "4":
                num1 = int(input("Enter 1st Number"))
                num2 = int(input("Enter 2nd Number"))
                print(f"{num1} / {num2} = {basic.div(num1, num2)}")
            case "5":
                num1 = int(input("Enter 1st Number"))
                num2 = int(input("Enter 2nd Number"))
                print(f"{num1} % {num2} = {adv.mod(num1, num2)}")
            case "6":
                num1 = int(input("Enter 1st Number"))
                num2 = int(input("Enter 2nd Number"))
                print(f"{num1} sqrt {num2} = {adv.sqrt(num1, num2)}")
            case _:
                print("Invalid option")
        print("Done")
    return None

if __name__ == "__main__":
    # Include standalone code to run if running as a program (not a module)
    main()
    sys.exit(0)
        