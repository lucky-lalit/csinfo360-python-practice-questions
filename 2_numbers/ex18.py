# Exercise 18: Abundant Number
# Description: Write a program to check if the sum of proper divisors exceeds the number.
# Example:
# Input: 12
# Output: Abundant (1+2+3+4+6 = 16 > 12)

inp_num = int(input("Enter the number: "))
sum = 0
i = 0
while i <= inp_num / 2:
    i = i + 1
    if inp_num % i == 0:
        sum = sum + i
# print(sum)
if sum > inp_num:
    print("Abundant")
else:
    print("Not Abundant")
