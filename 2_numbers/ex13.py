# Exercise 13: Perfect Square
# Description: Write a program to check if a number is the square of an integer.
# Example:
# Input: 49
# Output: Perfect Square (7Ã—7)

inp_num = int(input("Enter the Number to check for perfect square: "))
for i in range(inp_num + 1):
    if i * i == inp_num:
        print("perfect square")
        quit()
print("not perfect square")
