"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 19.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 19.
 #версия Python: 3.9
"""
a = float(input("Введите число А:"))
x = a
if x <= 2:
    fx = x**2 + 4*x + 5
    print("x <= 2; f(a) =:", fx)
else:
    fx = 1 / (x**2 + 4*x + 5)
    print("x > 2; f(a) =:", fx)
