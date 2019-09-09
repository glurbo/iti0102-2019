"""Ask user a shape and a radius or a side length and calculate the shape area."""

import math
shape = input("Please insert geometric shape:")
area = None

if shape == "circle":
    radius = input("Please insert radius in cm:")
    area = math.pi * (float(radius) ** 2)

elif shape == "square":
    length = input("Please insert side length in cm:")
    area = float(length) ** 2

elif shape == "triangle":
    length = input("Please insert side length in cm:")
    area = math.sqrt(3) / 4 * (float(length) ** 2)

else:
    print("Shape is not supported.")
    exit()

print(f"The area is {round(float(area), 2)} cm^2")
