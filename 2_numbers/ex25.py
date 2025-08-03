# Exercise 25: Sunny Number
# Description: Write a program to check if a number+1 is a perfect square.
# Example:
# Input: 24
# Output: Sunny (24+1=25 is 5Â²)

inp_num = int(input("Enter the Number: "))
i = 0
while i <= inp_num + 1:
    i = i + 1
    if inp_num + 1 == i * i:
        print("Sunny")
        quit()
print("Not Sunny")
