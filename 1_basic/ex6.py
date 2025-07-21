# 6. Write a program to input the basic salary of an employee and calculate the gross salary using standard allowances.

basic_salary = input("Enter the Basic Salary: ")
basic_salary = float(basic_salary)
gross_salary = basic_salary + (basic_salary * 0.5) + (basic_salary * 0.15)
print(gross_salary)
