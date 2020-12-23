"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 41.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 41.
 #версия Python: 3.9
"""
import random

N = int(input("Количество элементов массива"))
A = [1,5,3,-4]

print(A)

a = 0
for i in range(N):
    if A[i] >= 0:
        break
    if A[i] < 0:
        for i in range(N):
            if A[i-1] < A[i]:
                a = 0
            else:
                a =1
                break
        A[i] = A[i] - 1
        
if (a == 0):
    print("Возрастающая")
    
else:
    print("Убывающая")
