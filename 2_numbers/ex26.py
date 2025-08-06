# Exercise 26: Disarium Number
# Description: Write a program to check if a number equals the sum of its digits raised to their respective positions.
# Example:
# Input: 135
# Output: Disarium (1Â¹ + 3Â² + 5Â³ = 135)

inp_num = input("Enter the number: ")
count = 0
sum = 0
for i in inp_num:
    count = count + 1
    sum = sum + int(i) ** count
if sum == int(inp_num):
    print("Disarium")
else:
    print("Not Disarium")
