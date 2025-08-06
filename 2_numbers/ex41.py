# Exercise 41: Spy Numbers in Range
# Description: Write a program to find all Spy numbers between a given range.
# Description: Write a program to check if the sum of digits equals the product of digits.
# Example:
# Input: 1 to 1000
# Output: 1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 123, 132, 213, 231, 312, 321

inp_num_start = int(input("Enter the number from: "))
inp_num_stop = int(input("Enter the number to: "))

for i in range(inp_num_start, inp_num_stop + 1):
    sum = 0
    product = 1
    for j in str(i):
        product = product * int(j)
        sum = sum + int(j)
    if sum == product:
        print(i, end=" ")
