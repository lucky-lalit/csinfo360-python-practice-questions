# Exercise 14: Armstrong Number
# Description: Write a program to check if a number equals the sum of its digits each raised to the power of the number
#  of digits.
# Example:
# Input: 153
# Output: Armstrong (1Â³ + 5Â³ + 3Â³ = 153)

inp_num = input("Enter the number: ")
power = len(inp_num)
# print(type(power))
total = 0
for i in inp_num:
    # print(type(i))
    total = (int(i) ** power) + total
# print(total,type(total))
# print(inp_num,type(inp_num))
# print(total == inp_num)
if total == int(inp_num):
    # print(type(inp_num))
    print("Armstrong")
else:
    print("Not Armstrong")
