# 32. Write a program to calculate the area and perimeter of a rectangle given its length and breadth.

inp_length = float(input("Enter the length: "))
inp_breadth = float(input("Enter the breadth: "))

print(f"The area of the rectangle: {inp_breadth*inp_length}")
print(f"The perimeter of the rectangle: {2 * (inp_length + inp_breadth)}")
