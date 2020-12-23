"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 50.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 50.
 #версия Python: 3.9
"""
import random
N = int(input("Количество элементов в массиве "))
A = [random.randint(-5, 5) for i in range(0, N)]

print(A)

S = 0
K = 0
L = 0

for i in range(N):
    if A[i]%3 == 0:
        S = S + 1
    if A[i]%2 == 0:
        K = K + 1
        L = L + A[i]
F = L/K
A.append(F)
A.insert(0,S)

print(F)
print(S)
print(A)
