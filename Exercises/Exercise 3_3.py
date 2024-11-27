year = int(input("Please enter a year: "))

leap_check = year/4
leap_check2 = year/100

if int(leap_check) == leap_check and int(leap_check2) == leap_check2:
    print("Leap Year")
elif int(leap_check) == leap_check and float(leap_check2) == leap_check2:
    print("Leak Year")
elif float(leap_check) == leap_check and float(leap_check2) == leap_check2:
    print(" Not a Leap Year")
else:
    print("Error")