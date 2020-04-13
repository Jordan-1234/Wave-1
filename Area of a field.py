length = input("Enter a length in meters: ")
width = input("Enter a width in meters: ")

length = int(length)
width = int(width)
#Rounded to 2 decimal places
area = length * width
acres = area / 43560
acres = str(round(acres,2))
print("The area of the field is " + acres + " acres")