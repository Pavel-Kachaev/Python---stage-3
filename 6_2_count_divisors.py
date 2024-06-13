# -*- coding: cp1251 -*-
# Вводим натуральное число X
X = int(input("Введите натуральное число X: "))

count = 0
i = 1
while i*i <= X:
    if X % i == 0:
        if X // i == i:
            count += 1
        else:
            count += 2
    i += 1

# Выводим результат
print(f"Количество натуральных делителей числа {X} равно {count}")
