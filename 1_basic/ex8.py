# 8. Write a program to calculate compound interest given principal, rate, time, and number of times interest applied per year.

inp_principal = float(input("Enter principal: "))
inp_rate = float(input("Enter rate: "))
inp_time = float(input("Enter year: "))
inp_interest_year = float(input("Enter the interest applied per year: "))
compound_interest = (
    inp_principal * ((1 + 0.01 * (inp_rate / inp_interest_year)) ** (inp_interest_year * inp_time)) - inp_principal
)
print("compound interest: ", compound_interest)
