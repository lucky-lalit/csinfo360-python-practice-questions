# 31. Write a program to input a character and identify whether it is an uppercase letter, lowercase letter, digit, or
# special character.

inp_char = input("Enter the character: ")
if ord(inp_char) >= ord("A") and ord(inp_char) <= ord("Z"):
    print(f"{inp_char} is uppercase")
elif ord(inp_char) >= ord("a") and ord(inp_char) <= ord("z"):
    print(f"{inp_char} is lowercase")
elif ord(inp_char) >= ord("0") and ord(inp_char) <= ord("9"):
    print(f"{inp_char} is digit")
else:
    print(f"{inp_char} is special_character")


# capital = []
# for uppercase in range(65,91):
#     capital.append(chr(uppercase))
# if inp_char  in capital:
#     print(f'{inp_char} is uppercase')
#     quit()

# small = []
# for lowercase in range(97,122):
#     small.append(chr(lowercase))
# if inp_char in small:
#     print(f'{inp_char} is lowercase')
#     quit()

# digit = []
# for num in range(48,58):
#     digit.append(chr(num))
# if inp_char in digit:
#     print(f'{inp_char} is digit')
#     quit()
# else:
#     print(f'{inp_char} is special character')
