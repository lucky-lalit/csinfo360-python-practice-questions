# 14. Write a program to swap the values of two variables without using a third variable.

num1 = float(input("Enter the num1: "))
num2 = float(input("Enter the num2: "))

# num1, num2 = num2, num1
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("The swapped numbers are num1: ", num1, "and num2: ", num2)
