# Exercise 1: Sum of First N Natural Numbers
# Description: Write a program to calculate the sum of the first n natural numbers.
# Terminology: Natural numbers are positive integers starting from 1 (1, 2, 3, ...).
# Example:
# Input: n = 5
# Output: 15 (1+2+3+4+5)

inp_num = int(input("Enter the Numder: "))
# sum = 0
# while num > 0:
#     # print(num)
#     sum = sum + num
#     # print(sum)
#     num = num -1
# print(sum)

sum = 0
for i in range(1, inp_num + 1):
    sum = sum + i
print(sum)
