# 46. Write a program to calculate the surface area and volume of a cone using its radius and height.

inp_radius = float(input("Enter the radius: "))
inp_height = float(input("Enter the height: "))

surface_area = 3.14 * inp_radius * (inp_radius + ((inp_radius * inp_radius) + (inp_height * inp_height)) ** 0.5)
volume = 1 / 3 * 3.14 * inp_radius * inp_radius * inp_height

print(f"The Surface Area of cone: {surface_area}")
print(f"The volume of cone: {volume}")
