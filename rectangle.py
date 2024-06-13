# -*- coding: cp1251 -*-
# Ввод сторон прямоугольника
side1 = float(input("Введите длину первой стороны прямоугольника: "))
side2 = float(input("Введите длину второй стороны прямоугольника: "))

# Расчет площади и периметра
area = side1 * side2
perimeter = 2 * (side1 + side2)

# Вывод результатов
print("Площадь")
print(area)
print("Периметр")
print(perimeter)
