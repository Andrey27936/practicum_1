"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 40.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 40.
 #версия Python: 3.9
"""
import random

N = int(input("Количество элементов массива"))
A = [random.randint(-10,10) for i in range(0, N)]

print(A)
for i in range(N):
    if A[i] < 0:
        A[i] = A[i]**2
print(A)
