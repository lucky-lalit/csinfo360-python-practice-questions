# Exercise 16: Perfect Number
# Description: Write a program to check if a number equals the sum of its proper divisors (excluding itself).
# Example:
# Input: 28
# Output: Perfect (1+2+4+7+14 = 28)

inp_num = int(input("Enter the number: "))
total = 0
for i in range(1, inp_num):
    if inp_num % i == 0:
        total = total + i
if inp_num == (total):
    print("Perfect")
else:
    print("Not Perfect")
