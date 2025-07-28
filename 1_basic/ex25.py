# 25. Write a program to input a character and determine whether it is a vowel or consonant.

inp_char = str(input("Enter a character: "))
lower_char = inp_char.lower()
# print(lower_char)
# char_list = []
# char_list.append(inp_char)
vowels = ["a", "e", "i", "o", "u"]
for char in vowels:
    if char == lower_char:
        print(f"{inp_char} is vowel")
        quit()
    # else:
print(f"{inp_char} is consonant")
# break


# if inp_char in vowels:
#     print(f'{inp_char} is vowel')
# else:
#     print(f'{inp_char} is consonant')
# if ch
# print(inp_char == 'a' ,inp_char == 'e',1 or 2, 0 or 5,0 or 0 or False or [])
# if inp_char == 'a' or inp_char == 'e' or inp_char == 'i' or inp_char == 'o' or inp_char == 'u':
#     print(f'{inp_char} is vowel')
# else:
#     print(f'{inp_char} is consonant')


# if inp_char == 'a':
#     print(f'{inp_char} is vowel')
# elif inp_char == 'e':
#     print(f'{inp_char} is vowel')
# elif inp_char == 'i':
#     print(f'{inp_char} is vowel')
# elif inp_char == 'o':
#     print(f'{inp_char} is vowel')
# elif inp_char == 'u':
#     print(f'{inp_char} is vowel')
# else:
#     print(f'{inp_char} is consonant')
