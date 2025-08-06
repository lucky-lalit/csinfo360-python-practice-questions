# Exercise 44: Disarium Numbers in Range
# Description: Write a program to find all Disarium numbers between a given range.
# Description: Write a program to check if a number equals the sum of its digits raised to their respective positions.
# Example:
# Input: 1 to 200
# Output: 1, 2, 3, 4, 5, 6, 7, 8, 9, 89, 135, 175

inp_num_start = int(input("Enter the number from: "))
inp_num_stop = int(input("Enter the number to: "))

for i in range(inp_num_start, inp_num_stop + 1):
    sum = 0
    # print('i',i)
    power = 0
    for j in str(i):
        j = int(j)
        # print('j',j)
        # print('sum',sum)
        power = power + 1
        sum = sum + j**power
        # print('sum_after',sum)
    if sum == i:
        print(i, end=" ")
