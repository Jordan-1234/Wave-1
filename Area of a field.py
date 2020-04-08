length = input("Enter a length in meters: ")
width = input("Enter a width in meters: ")

length = int(length)
width = int(width)

area = length * width
acres = area // 43560
acres = str(acres)
print("The area of the field is " + acres + " acres")

