"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 38.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 38.
 #версия Python: 3.9
"""
import array
import random

N = int(input("Введите количество элементов массива "))
K = int(input("Позиция K "))
M = int(input("количество элементов для вычитания "))
A = [random.randint(0, 100) for i in range(0, N)]
print(A)

A.insert(K,M)
print(A)

A.delete(K,M)
