# 40. Write a program to calculate the area of a trapezoid given its two bases and height.

inp_base1 = float(input("Enter the base1: "))
inp_base2 = float(input("Enter the base2 : "))
inp_height_base = float(input("Enter the height: "))

area = (inp_height_base * (inp_base1 + inp_base2)) / 2

print(f"The Area of Trapezoid: {area}")
