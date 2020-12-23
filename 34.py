"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 34.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 34.
 #версия Python: 3.9
"""
import random

N = int(input("Введите количество элементов массива "))
a = [random.randint(0, 100) for i in range(0, N)]
print(a)
for i in range(len(a) // 2):
    a[i], a[i + len(a) // 2] = a[i + len(a) // 2], a[i]
    
print(a)
