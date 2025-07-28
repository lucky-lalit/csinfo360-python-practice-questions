# 44. Write a program to calculate the surface area and volume of a cylinder using its radius and height.

inp_radius = float(input("Enter the radius of the of cylinder: "))
inp_height = float(input("Enter the height of the of cylinder: "))

volume = 3.14 * (inp_radius**2) * inp_height
surface_area = 2 * 3.14 * inp_radius * (inp_radius + inp_height)

print(f"The volume of the sphere: {volume}")

print(f"The surface area of the sphere: {surface_area}")
