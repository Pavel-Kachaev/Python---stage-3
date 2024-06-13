# -*- coding: cp1251 -*-
word = input("Введите слово из маленьких латинских букв: ")
vowels = ['a', 'e', 'i', 'o', 'u']
vowelscount = 0
consonantscount = 0

for letter in word:
    if letter in vowels:
        vowelscount += 1
    elif letter.isalpha():
        consonantscount += 1
    else:
        print("false")

if consonantscount == 0:
    print("false")
else:
    print("true")
    print(f"Количество гласных букв: {vowelscount}")
    print(f"Количество согласных букв: {consonantscount}")
