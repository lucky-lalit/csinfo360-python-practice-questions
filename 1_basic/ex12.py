# 12. Write a program to convert a given number of days into equivalent years, months, and weeks.
# 365

inp_days = int(input("Enter the number of days: "))

years = inp_days // 365
year_remaining_days = inp_days % 365
months = year_remaining_days // 30
month_remaining_days = year_remaining_days % 30
week = month_remaining_days // 7
days = month_remaining_days % 7

print("There are", years, "years", months, "months", week, "weeks", days, "days in given", inp_days, "days")
