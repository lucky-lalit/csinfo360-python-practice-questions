# 11. Write a program to convert a distance in kilometers to both miles and meters.

inp_dis = float(input("Enter the distance in kilometer: "))

km_to_miles = inp_dis * 0.621371
km_to_meters = inp_dis * 1000

print("The Distance in miles", km_to_miles, "and in meters", km_to_meters)
