# 42. Write a program to calculate the surface area and volume of a sphere given its radius.

inp_radius = float(input("Enter the radius: "))

print(f"The area of the sphere: {4*3.14*inp_radius**2}")

volume = 4 / 3 * (3.14 * inp_radius**3)
print(f"The volume of the sphere: {volume}")
