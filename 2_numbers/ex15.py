# Exercise 15: Strong Number
# Description: Write a program to check if a number equals the sum of the factorials of its digits.
# Example:
# Input: 145
# Output: Strong (1! + 4! + 5! = 145)


inp_num = input("Enter the number: ")
product = 1
total = 0
for i in inp_num:
    #     # print(type(i),type(product))
    # print(i)
    product = 1
    for j in range(1, int(i) + 1):
        #         print(j,'product',product)
        # product = 1
        product = int(j) * product
    #         print('after_product',product)
    #         # print(product,type(product))
    #         # print('debug1',total)
    # print('debug2',int(product))
    total = total + int(product)
if total == int(inp_num):
    print("Strong")
else:
    print("Not Strong")

# for


# product = 1
# for i in range(1,(int(inp_num)+1)):
#     product=product*i
# print(product)
