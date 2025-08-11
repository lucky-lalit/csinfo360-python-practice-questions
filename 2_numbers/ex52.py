# Exercise 52: Nth Strong Number
# Description: Write a program to find the nth Strong number.
# Description: Write a program to check if a number equals the digit_sum of the factorials of its digits.
# Example:
# Input: 3
# Output: 145 (sequence: 1, 2, 145, 40585...)

inp_num = int(input("Enter the nth number for nth strong number: "))


# inp_num_start = int(input('enter the number start: '))
# inp_num_stop = int(input('Enter the number end: '))

# for i in range(inp_num_start,inp_num_stop+1):
#     # product = 1
#     digit_sum = 0
#     for j in str(i):
#         product = 1
#         for k  in range(1,int(j)+1):
#             product = product * int(k)
#             digit_sum = digit_sum + product
#             # print(digit_sum)

# if digit_sum == i:
#     print(i)
# print(type(j))


def check_strong(num):
    digit_sum = 0
    # product = 1
    for i in str(num):
        # digit_sum = 0
        product = 1
        # print('debug2',i)
        for j in range(1, int(i) + 1):
            # print('debug1',j)
            # print('product',product)
            # print('digit_sum',digit_sum)
            product = product * j
        digit_sum = digit_sum + product
        # print('debug1',j)
        # print('product',product)
        # print('digit_sum',digit_sum)
        # print(j)
    # print(digit_sum,num)
    if digit_sum == num:
        return True
    else:
        return False


# print(check_strong(2))

i = 1
strong_count = 0
nth_strong = None
while strong_count < inp_num:
    if check_strong(i):
        strong_count = strong_count + 1
        nth_strong = i
    i = i + 1
print(nth_strong)

# correct
