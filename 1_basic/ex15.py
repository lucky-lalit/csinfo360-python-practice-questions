# 15. Write a program to swap three numbers such that the first becomes the second,
# the second becomes the third, and the third becomes the first.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

temp = num1
num1 = num2
num2 = num3
num3 = temp

print("The Swapped Numbers are num1", num1, "num2", num2, "num3", num3)
