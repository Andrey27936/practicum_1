"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 11.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 11.
 #версия Python: 3.9
"""
A = int(input("Введите длину коробки:"))
B = int(input("Введите ширину коробки:"))
C = int(input("Введите высоту коробки:"))
M = int(input("Введите ширину двери:"))
X = int(input("Введите высоту двери:"))
if ((C <= X and B <=X)
    or (C<=X and A <=X)
    or (A <= X and B <= X)):
    print("Коробка пройдет в дверь")
else:
    print("Коробка не пройдет в дверь")
