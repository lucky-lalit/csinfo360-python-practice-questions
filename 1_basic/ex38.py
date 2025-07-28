# 38. Write a program to compute the area and perimeter of a rhombus given its diagonals and side.

inp_diagonal = float(input("Enter the diagoanl of the rhombus: "))
inp_side = float(input("Enter the side of the rhombus: "))

inp_diagonal2 = ((4 * inp_side**2) - inp_diagonal**2) ** 0.5
print(f"The area of the rhombus: {inp_diagonal * inp_diagonal2*0.5}")

print(f"The perimeter of the rhombus: {4*inp_side}")
