# 21. Write a program to print all odd numbers from 1 up to a user-defined number n.

num_inp = int(input("Enter a Number: "))

for num in range(1, num_inp + 1):
    if num % 2 == 1:
        print(num)
