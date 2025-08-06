# Exercise 27: Pronic Number
# Description: Write a program to check if a number is the product of two consecutive integers.
# Example:
# Input: 42
# Output: Pronic (6Ã—7=42)

inp_num = int(input("Enter the NUmber: "))
# product = 1
# i =  0
# while i < inp_num//2:
#     i = i + 1
for i in range(1, inp_num // 2):
    # print('debug1',i,i+1,'=',i*(i+1))
    if i * (i + 1) == inp_num:
        print("Pronic")
        quit()
print("Not Pronic")
