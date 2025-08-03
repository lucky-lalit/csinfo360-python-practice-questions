# Exercise 22: Neon Number
# Description: Write a program to check if the sum of digits of a number's square equals the number.
# Example:
# Input: 9
# Output: Neon (9Â²=81 â†’ 8+1=9)

inp_num = int(input(("Enter the NUmber: ")))
sqr_num = inp_num * inp_num
sum = 0
for i in str(sqr_num):
    sum = sum + int(i)

if int(sum) == inp_num:
    print("Neon")
else:
    print("Not Neon")
