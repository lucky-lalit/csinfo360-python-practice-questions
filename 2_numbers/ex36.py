# Exercise 36: Harshad Numbers in Range
# Description: Write a program to find all Harshad numbers between a given range.
# Example:
# Input: 1 to 100
# Output: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, 27, 30, 36, 40, 42, 45, 48, 50, 54, 60, 63, 70, 72, 80, 81,
#  84, 90, 100

inp_num_start = int(input("Enter the number from: "))
inp_num_stop = int(input("Enter the number to: "))

for i in range(inp_num_start, inp_num_stop + 1):
    sum = 0
    for j in str(i):
        sum = sum + int(j)
    if i % sum == 0:
        print(i, end=" ")
