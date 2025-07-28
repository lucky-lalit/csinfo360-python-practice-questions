# 29. Write a program to generate and print the multiplication table of a given number.

inp_num = float(input("Enter the Number for the required table: "))
# print(f'Product: {inp_num*inp_num}')

for multiplier in range(1, 11):
    multiple = multiplier * inp_num
    print(f"5 x {multiplier} = {multiple}")
