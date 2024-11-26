fuel_consumption = 2.25     #consumption per lap
race_length = 45            #number of laps
qualifying_time = 80.45     #seconds per lap
qualifying_fuel = 5         #kg
time_penalty_per_kg = 0.035 #seconds

min_fuel = (fuel_consumption*race_length) * 1.5
print("Min fuel required = " + str(round(min_fuel, 2)) + "kg")

first_lap = qualifying_time + ((min_fuel - 5)*time_penalty_per_kg)
print("Initial lap time is = " + str(round(first_lap, 2)) + "s")