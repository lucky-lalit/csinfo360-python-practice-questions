# 17. Write a program to input marks in five subjects and calculate the total marks, average marks, and percentage.

maths_marks = float(input("Enter marks in math subject: "))
english_marks = float(input("Enter marks in english subject: "))
science_marks = float(input("Enter marks in science subject: "))
hindi_marks = float(input("Enter marks in hindi subject: "))
geography_marks = float(input("Enter marks in geography subject: "))

total = maths_marks + english_marks + science_marks + hindi_marks + geography_marks
average = total / 5
percentage = (total / 500) * 100

print("The student got total", total, "marks and average marks is", average, ",the percentage is", percentage)
