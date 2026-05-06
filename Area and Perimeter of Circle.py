import math

# 1. Get the radius from the user
# Use float() so the user can enter decimal numbers
radius = float(input("Enter the radius of the circle: "))

# 2. Get the diameter from the user
# Use float() so the user can enter decimal numbers
diameter = float(input("Enter the diameter of the circle: "))

# 3. Calculate the Area using the formula: π * r^2
area = math.pi * radius ** 2

# 4. Calculate the Perimeter (Circumference) using the formula: 2 * π * r
perimeter = 2 * math.pi * radius

# 5. Calculate the radius of the Area using: 
# r = √(Area / π) or r = Perimeter / (2 * π)
radius = math.sqrt(area / math.pi) 

# 6. Calculate the diameter of the Perimeter (Circumference) using: 
# d = (Perimeter / π) or d = 2 * r
diameter = perimeter / math.pi

# 7. Display the results rounded to 2 decimal places
print(f"Area of the circle: {round(area, 2)}")
print(f"Perimeter (Circumference) of the circle: {round(perimeter, 2)}")

# 8. Display the radius and diameter based on Area and Perimeter respectively
print(f"Radius of the circle based on Area: {round(radius, 2)}")
print(f"Diameter of the circle based on Perimeter: {round(diameter, 2)}")