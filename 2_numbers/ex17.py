# Exercise 17: Harshad Number
# Description: Write a program to check if a number is divisible by the sum of its digits.
# Example:
# Input: 18
# Output: Harshad (1+8=9, and 18 is divisible by 9)

inp_num = input("Enter the number: ")
sum = 0
for i in inp_num:
    sum = sum + int(i)
if int(inp_num) % sum == 0:
    print("Harshad")
else:
    print("Not Harshad")
