# 13. Write a program to swap the values of two variables using a third variable.


num1 = float(input("Enter the num1: "))
num2 = float(input("Enter the num2: "))

num3 = num1
num1 = num2
num2 = num3
print("The swapped numbers are num1 =", num1, "and", "num 2 =", num2)
