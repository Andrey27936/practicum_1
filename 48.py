"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 48.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 48.
 #версия Python: 3.9
"""
import random

N = int(input("Количество элементов в массиве"))
A = [random.randint(-2, 2) for i in range(0, N)]

print(A)

for i in range(N):
    if A[i] == 0:
        A[i] = A[i-1] + A[i-2]
        
print(A)
