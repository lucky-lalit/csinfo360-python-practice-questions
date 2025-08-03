# Exercise 9: Find Factorial
# Description: Write a program to calculate the factorial of a number.
# Example:
# Input: 5
# Output: 120 (5Ã—4Ã—3Ã—2Ã—1)

import math

inp_num = int(input("Enter the number to calculate the factorial: "))
# print(math.factorial(inp_num))
product = 1
for i in range(1, inp_num + 1):
    product = product * i
print(product)
