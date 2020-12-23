"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 46.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 46.
 #версия Python: 3.9
"""
import random

N = int(input("Количество элементов массива"))
T = int(input("Положительное число"))
A = [random.randint(-10, 10) for i in range(0, N)]

print(A)

S = 0
for i in range(N):
    if A[i] > 0:
        S = S + A[i]
K = T/S
for i in range(N):
    if A[i] > 0:
        A[i] += (A[i]*K)
        
print(K)
print(A)
