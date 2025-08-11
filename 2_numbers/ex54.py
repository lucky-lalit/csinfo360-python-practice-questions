# Exercise 54: Nth Harshad Number
# Description: Write a program to find the nth Harshad number.
# Description: Write a program to check if a number is divisible by the digit_sum of its digits.
# Example:
# Input: 10
# Output: 10 (sequence: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12...)

inp_num = int(input("Enter the nth number to find nth Harshad number: "))


def check_Harshad(num):
    digit_sum = 0
    for i in str(num):
        digit_sum = digit_sum + int(i)
        # print(i)
    if num % digit_sum == 0:
        return True
    else:
        return False


# print(check_Harshad(inp_num))

i = 1
count = 0
nth_harshad = None
while count < inp_num:
    if check_Harshad(i):
        count = count + 1
        nth_harshad = i
    i = i + 1
print(nth_harshad)

# correct
