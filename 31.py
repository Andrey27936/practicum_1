"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 31.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 31.
 #версия Python: 3.9
"""
import random

n = 25
a = [random.randint(0, 100) for i in range(n)]
print(a)
N = 1
while N < n - 1:
    for i in range(n - N):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    N += 1
    
print(a)
