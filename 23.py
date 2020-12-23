"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 23.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 23.
 #версия Python: 3.9
"""
import math
x = float(input("Введите вещественное число x:"))
y = float(input("Введите вещественное число y:"))
if x > y:
    z = math.sqrt(x * y)
    print(z)
else:
    z = math.log(x + y, math.e)
    print(z)
