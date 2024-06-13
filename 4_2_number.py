# -*- coding: cp1251 -*-
# Ввод пятизначного целого числа
num = int(input("Введите пятизначное целое число: "))

# Извлечение разрядов числа

tens_of_thousands = int(num // 10000) %10
print(tens_of_thousands)
thousands = int(num // 1000) %10
print(thousands)
hundreds = int(num // 100) %10
print(hundreds)
tens = (num // 10) %10
print(tens)
units = int(num % 10)
print(units)
# Вычисление результата по формуле
result = (tens ** units) * hundreds / (tens_of_thousands - thousands)

# Вывод результата
print(result)
