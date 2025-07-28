# 43. Write a program to calculate the surface area and volume of a hemisphere given its radius.

inp_radius = float(input("Enter the radius of the hemisphere: "))

surface_area = 3 * 3.14 * inp_radius**2
volume_sphere = 2 / 3 * (3.14 * inp_radius**3)

print(f"The area of the hemisphere {surface_area}")
print(f"The volume of the hemisphere {volume_sphere}")
