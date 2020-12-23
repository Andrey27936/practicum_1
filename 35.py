"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 47.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 47.
 #версия Python: 3.9
"""
import random

N = int(input("Количество элементов массива"))
B = int(input("Элемент массива 1"))
C = int(input("Элемент массива 2"))
A = [random.randint(-10, 10) for i in range(0, N)]

print(A)

C = C + 1
del A[B:C]

print(A)
