# Exercise 2: Calculate 1/n!
# Description: Write a program to compute the reciprocal of a factorial (1 divided by n factorial).
# Terminology: Factorial (n!) is the product of all positive integers from 1 to n (e.g., 4! = 4Ã—3Ã—2Ã—1 = 24).
# Example:
# Input: n = 4
# Output: 0.041666... (1/24)

inp_num = int(input("Enter the number: "))
product = 1
for i in range(1, inp_num + 1):
    product = product * i
print(1 / product)
