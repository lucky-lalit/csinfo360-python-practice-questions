# Exercise 32: Perfect Squares in Range
# Description: Write a program to find all perfect square numbers between a given range.
# Example:
# Input: 10 to 50
# Output: 16, 25, 36, 49
# import math
inp_num_start = int(input("Enter the number from: "))
inp_num_stop = int(input("Enter the number to: "))

count = 0
for i in range(inp_num_start, inp_num_stop + 1):
    for j in range(i + 1):
        if j * j == i:
            if count > 0:
                print(', ',end = '')
            print(j * j, end="")
            count = count +1
            break
    # if i == math.sqrt(i)*math.sqrt(i):
    # print(i)
