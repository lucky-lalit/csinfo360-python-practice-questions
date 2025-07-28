# 39. Write a program to compute the area and perimeter of a regular pentagon.

import math

inp_side = float(input("Enter the side of the pentagon: "))

print(f"Area of the pentagon {5 * (inp_side**2) *math.tan((3*math.pi)/10)/4}")

print(f"primeter of the pentagon {5*inp_side}")
