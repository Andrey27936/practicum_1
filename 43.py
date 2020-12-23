"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 43.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 43.
 #версия Python: 3.9
"""
import random

N = int(input("Количество элементов массива"))
A = [random.randint(-10,10) for i in range(0,N)]
Ao = []
Ap = []

for i in range(N):
    if A[i] > 0:
        Ap.append(A[i])
    if A[i] < 0:
        Ao.append(A[i])
        
print("Отрицательные",Ao)
print("Положительные",Ap)
