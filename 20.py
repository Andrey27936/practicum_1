"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 20.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 20.
 #версия Python: 3.9
"""
import math
x = int(input("Введите число для проверки:"))
a = int(input("Укажите начало промежутка:"))
b = int(input("Укажите конец промежутка:"))

if math.fabs(a) <= math.fabs(x) <= math.fabs(b):
    print("Число ",x, " Принадлежит множеству [",a,",",b,"]")
else:
    print("Число ",x, " не принадлежит множеству [",a,",",b,"]")
