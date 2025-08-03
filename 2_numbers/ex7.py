# Exercise 7: Calculate GCD/HCF
# Description: Write a program to find the Greatest Common Divisor (GCD) or Highest Common Factor (HCF) of two numbers.
# Terminology: GCD is the largest positive integer that divides both numbers without remainder.
# Example:
# Input: 12 and 18
# Output: 6

inp_num1 = int(input("Enter the number to find HCF: "))
inp_num2 = int(input("Enter the number to find HCF: "))
i = 1
highest = None
# while i >= inp_num1 and i <= inp_num2:
while i < inp_num2:
    i = i + 1
    if inp_num1 % i == 0 and inp_num2 % i == 0:
        # print('debug1')
        if (highest is None) or (highest < i):
            highest = i
            # print('debug2')
print(highest)
