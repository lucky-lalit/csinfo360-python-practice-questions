# 7. Write a program to calculate simple interest using principal, rate of interest, and time.

inp_principle = float(input("Enter principle: "))
inp_rate_interest = float(input("Enter rate of interest: "))
inp_year = float(input("Enter the year: "))

simple_interest = (inp_principle * (inp_rate_interest) * inp_year) / 100
print("Simple Interest :", simple_interest)
