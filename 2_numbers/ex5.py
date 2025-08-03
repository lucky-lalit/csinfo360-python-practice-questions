# Exercise 5: Sum of Digits
# Description: Write a program to calculate the sum of all digits of a number.
# Example:
# Input: 1234
# Output: 10 (1+2+3+4)

# b = '1234'
# print(a[0])
inp_num = input("Enter the number: ")
# len_inp = len(inp_num)
sum = 0
for i in inp_num:
    sum = sum + int(i)
print(sum)
# i = 0
# while i < len_inp:
# print(i)
#     val = inp_num[i]
#     sum =sum + int(inp_num[i])
#     i = i + 1
# print(sum)
