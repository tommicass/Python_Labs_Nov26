
try:
    var = int(input("Start Number: "))
except:
    print("invalid integer, please enter a valid number")
    
while var >= 2:
    var -= 2
    print(var)

for var in range(var, -1, -2):
    print(var)