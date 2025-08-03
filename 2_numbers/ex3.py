# Exercise 3: Compute x^n / n!
# Description: Write a program to compute x raised to power n divided by n factorial.
# Terminology: Exponentiation (x^n) and factorial (n!) combined in one operation.
# Example:
# Input: x = 2, n = 3
# Output: 1.333... (8/6)

exp_base = int(input("Enter the base for exponential: "))
inp_pow_fac = int(input("Enter the number for raise to: "))
product = 1
for i in range(1, inp_pow_fac + 1):
    product = product * i
print((exp_base**inp_pow_fac) / product)
