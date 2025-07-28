# 22. Write a program to print all even numbers from 1 up to a user-defined number n.

num_inp = int(input('Enter the Number: '))

for num in range(1,num_inp+1):
    if num % 2 == 0:
        print(num)
