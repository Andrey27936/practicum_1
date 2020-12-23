"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 26.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 26.
 #версия Python: 3.9
"""
import math
A = float(input("Введите число А:"))
x = A
if x <= 0:
    fx = 0
    print("x <= 0; f(A) =:", fx)
elif 0 < x < 1:
    fx = x
    print("0 < x < 1; f(A) =:", fx)
else:
    fx = math.pow(x, 4)
    print("x >= 1; f(A) =:", fx)
