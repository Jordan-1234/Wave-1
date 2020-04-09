import math
radius = float(input("Enter in the radius of the cylinder "))
height = float(input("Enter in the height of the cylinder "))
cylinder_Area = (2 * math.pi * pow(radius,2) * height)
print('The volume of the cylinder will be ' + str(round(cylinder_Area,1)))