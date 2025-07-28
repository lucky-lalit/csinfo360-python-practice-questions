# 27. Write a program to check whether a given number is positive, negative, or zero.

inp_num = float(input("Enter the NUmber: "))

if inp_num > 0:
    print(f"{inp_num} is Positive Number")
elif inp_num == 0:
    print(f"{inp_num} is Zero")
else:
    print(f"{inp_num} is Negative")
