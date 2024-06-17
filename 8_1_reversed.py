# -*- coding: cp1251 -*-
# Считываем количество чисел
N = int(input())

# Создаем пустой список для хранения чисел
numbers = []

# Считываем числа и добавляем их в список
for _ in range(N):
    num = int(input())
    numbers.append(num)

# Используем reversed для переворачивания списка
reversed_numbers = list(reversed(numbers))

# Выводим перевернутый массив чисел
for num in reversed_numbers:
    print(num)
