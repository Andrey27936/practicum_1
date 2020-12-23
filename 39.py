"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 39.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 39.
 #версия Python: 3.9
"""
import random

N = int(input("Введите количество элементов массива "))
A = [random.randint(-1, 1) for i in range(0, N)]

print(A)
B = filter(bool, A)
print(list(B))
