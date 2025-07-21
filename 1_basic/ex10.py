# 10. Write a program to convert temperature from Fahrenheit to Celsius.

inp_temp = float(input("Enter tmeperature in Fahrenheit: "))

temp_cel = (inp_temp - 32) * 5 / 9

print("Temperature in Celsius: ", temp_cel)
