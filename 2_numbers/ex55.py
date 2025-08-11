# Exercise 55: Nth Abundant Number
# Description: Write a program to find the nth abundant number.
# Description: Write a program to check if the divisor_sum of proper divisors exceeds the number.
# Example:
# Input: 5
# Output: 30 (sequence: 12, 18, 20, 24, 30, 36...)

inp_num = int(input("Enter the nth number to get nth abundant number: "))


def check_abundant(num):
    divisor_sum = 0
    for i in range(1, num):
        if num % int(i) == 0:
            divisor_sum = divisor_sum + int(i)
    if divisor_sum > num:
        return True
    else:
        return False


# print(check_abundant(inp_num))

i = 0
count = 0
nth_abundant = None
while count < inp_num:
    if check_abundant(i):
        count = count + 1
        nth_abundant = i
    i = i + 1
print(nth_abundant)

# for i in range(1,2):
#     print('hlo')
#     print(i)

# correct
