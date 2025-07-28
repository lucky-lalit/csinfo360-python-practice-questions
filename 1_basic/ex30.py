# 30. Write a program to input three numbers and find the smallest among them.

inp_num1 = float(input("Enter the First Number: "))
inp_num2 = float(input("Enter the Second Number: "))
inp_num3 = float(input("Enter the Third Number: "))

if inp_num1 < inp_num2 and inp_num1 < inp_num3:
    print(f"{inp_num1} is the smallest")
elif inp_num2 < inp_num1 and inp_num2 < inp_num3:
    print(f"{inp_num2} is the smallest")
else:
    print(f"{inp_num3} is the smallest")
