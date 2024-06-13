# -*- coding: cp1251 -*-
# Вводим целые числа A и B
A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))

# Выводим все четные числа на отрезке от A до B
for num in range(A, B+1):
    if num % 2 == 0:
        print(num, end=" ")
