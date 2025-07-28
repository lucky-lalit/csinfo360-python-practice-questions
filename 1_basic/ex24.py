# 24. Write a program to check whether a given number is even or odd.

inp_num = int(input("Enter the number to check odd or even: "))

if inp_num % 2 == 0:
    print(f"{inp_num} is even")
else:
    print(f"{inp_num} is odd")
