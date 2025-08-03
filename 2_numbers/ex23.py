# Exercise 23: Spy Number
# Description: Write a program to check if the sum of digits equals the product of digits.
# Example:
# Input: 123
# Output: Spy (1+2+3 = 1Ã—2Ã—3 = 6)


inp_num = input("Enter the Number: ")
sum = 0
product = 1
for i in inp_num:
    sum = sum + int(i)
    product = product * int(i)
if sum == product:
    print("spy")
else:
    print("not spy")
