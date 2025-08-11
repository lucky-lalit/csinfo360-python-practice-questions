# Exercise 51: Nth Armstrong Number
# Description: Write a program to find the nth Armstrong number.
# Description: Write a program to check if a number equals the sum of its digits each raised to the power of the number
# of digits.
# Example:
# Input: 5
# Output: 370 (sequence: 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370...)  correction  i/p 11

inp_index = int(input("Enter the number: "))
i = 0
count = 0
digit_sum = 0
armstrong_list = []
while True:
    if count == inp_index:
        print(armstrong_list[inp_index - 1])
        break
    i = i + 1
    # print(i)
    digit_sum = 0
    power = len(str(i))
    #     # print('len',len(str(i)))
    for j in str(i):
        digit_sum = digit_sum + int(j) ** power
        # print(sum)
    if digit_sum == i:
        armstrong_list.append(i)
        count = count + 1
# print()

# correct
