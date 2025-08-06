# Exercise 35: Perfect Numbers in Range
# Description: Write a program to find all Perfect numbers between a given range.
# Example:
# Input: 1 to 1000
# Output: 6, 28, 496

inp_num_start = int(input("Enter the number from: "))
inp_num_stop = int(input("Enter the number to: "))

for i in range(inp_num_start, inp_num_stop + 1):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum = sum + j
    if sum == i:
        print(sum, end=" ")
