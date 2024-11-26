from math import pi, tan, cos

barrel_height = 1
distance = 0.5
elevation = 80
velocity = 44

elevation = 80 * (pi/180)

height = barrel_height + (distance*tan(elevation))
- ((9.81*pow(distance,2))/(2*pow((velocity*cos(elevation)),2)))

print(round(height,2))