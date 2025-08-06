# Exercise 33: Armstrong Numbers in Range
# Description: Write a program to find all Armstrong numbers between a given range.
# Example:
# Input: 100 to 500
# Output: 153, 370, 371, 407

inp_num_start = int(input("Enter the number from: "))
inp_num_stop = int(input("Enter the number to: "))
# sum = 0
for i in range(inp_num_start, inp_num_stop + 1):
    # print(len(str(i)))
    # print('debug 1',i)
    sum = 0
    for j in str(i):
        # print('debug2',j)
        # print(j,end=' ')
        sum = sum + int(j) ** len(str(i))
    # print('debug4',sum)
    if i == sum:
        print(i, end=" ")
