# 23. Write a program to check whether a given year is a leap year or not.

inp_year = int(input("Enter the year to check for leap: "))

if inp_year % 400 == 0:
    print(f"{inp_year} is leap year")
# if inp_year % 4 == 0:
elif inp_year % 100 == 0:
    print(f"{inp_year} is not leap year")
# elif inp_year % 100 == 0:
#     print(f"{inp_year} is not leap year")10
elif inp_year % 4 == 0:
    print(f"{inp_year} is the leap year")
else:
    print(f"{inp_year} *else* is not leap year")
