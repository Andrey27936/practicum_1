"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 49.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 49.
 #версия Python: 3.9
"""
import random

N = int(input("Количество элементов в массиве"))
A = [random.randint(-1, 1) for i in range(0, N)]

print(A)

for i in range(N):
    if A[i] == 0 and A[i-1] == 0:
        print("Два подряд нуля в ",i-1,"и",i)
