# 5. Write a program to convert a given time in seconds into hours, minutes, and remaining seconds.

inp_sec = input("Enter time in seconds: ")
inp_sec = float(inp_sec)
hrs = inp_sec // 3600
remaining_sec = inp_sec % 3600
# print('debug1',remaining_sec)
min = remaining_sec // 60
# print('debug2',min)
sec = remaining_sec % 60
print("Hours =", hrs, "Minutes =", min, "Seconds =", sec)
