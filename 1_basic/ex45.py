# 45. Write a program to calculate the surface area and volume of a cuboid using its length, width, and height.

inp_length = float(input("Enter the length: "))
inp_width = float(input("Enter the width: "))
inp_height = float(input("Enter the height: "))

area_cuboid = 2 * ((inp_length * inp_height) + (inp_length * inp_width) + (inp_width * inp_height))

volume_cuboid = inp_height * inp_length * inp_width

print(f"The area of the cuboid: {area_cuboid}")

print(f"The volume of the cuboid: {volume_cuboid}")
