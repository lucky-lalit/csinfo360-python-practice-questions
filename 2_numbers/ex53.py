# Exercise 53: Nth Perfect Number
# Description: Write a program to find the nth perfect number.
# Description: Write a program to check if a number equals the div_sum of its proper divisors (excluding itself).
# Example:
# Input: 2
# Output: 28 (sequence: 6, 28, 496, 8128...)  (1+2+4+7+14 = 28)

inp_num = int(input("Enter the nth number for nth perfect number: "))


def check_perfect(num):
    div_sum = 0
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            div_sum = div_sum + i
    if div_sum == num:
        return True
    else:
        return False


# print(check_perfect(inp_num))


i = 1
count = 0
nth_sqr_num = None
while count < inp_num:
    # print('debug0')
    if check_perfect(i):
        count = count + 1
        nth_sqr_num = i
        # print(i)
        # print('debug 1')
    i = i + 1
# print('debug 2')
# if inp_num == nth_sqr_num:
print(nth_sqr_num)

# correct
