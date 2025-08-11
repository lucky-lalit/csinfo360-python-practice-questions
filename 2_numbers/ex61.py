# Exercise 61: Nth Sunny Number
# Description: Write a program to find the nth sunny number.
# Description: Write a program to check if a number+1 is a perfect square.
# (24+1=25 is 5Â²)
# Example:
# Input: 5
# Output: 35 (sequence: 3, 8, 15, 24, 35, 48...)

inp_num = int(input('Enter the nth number to get nth sunny number: '))

def check_sunny(num):
        # for j in range(1,num+2):
        #     if num + 1 == j*j:
        #         break
        # print(i+1,j)
        square_root = (num + 1)**0.5
        if num + 1 == int(square_root)*int(square_root) and num != 0:
            return True
        else:
            return False
# print(check_sunny(inp_num))

# for i in range(inp_num,inp_num+1):
#     print(i)

i = 0
count = 0
nth_sunny_number = None
while count < inp_num:
    if check_sunny(i):
        count = count + 1
        nth_sunny_number = i
    i = i + 1
print(nth_sunny_number)

# correct