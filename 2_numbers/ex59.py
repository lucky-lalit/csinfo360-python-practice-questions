# Exercise 59: Nth Spy Number
# Description: Write a program to find the nth spy number.
# Description: Write a program to check if the digit_sum of digits equals the product of digits.
# Example:
# Input: 5
# Output: 5 (sequence: 1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 123...)

inp_num = int(input("Enter the nth number to get the nth spy number: "))


def check_spy(num):
    if num == 0:
        return False
    digit_sum = 0
    product = 1
    for i in str(num):
        digit_sum = digit_sum + int(i)
        product = product * int(i)
    if digit_sum == product:
        return True
    else:
        return False


# print(check_spy(inp_num))

i = 1
count = 0
nth_spy_num = None
while count < inp_num:
    if check_spy(i):
        count = count + 1
        nth_spy_num = i
    i = i + 1
print(nth_spy_num)

# correct
