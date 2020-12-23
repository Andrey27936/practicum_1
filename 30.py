"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 30.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 30.
 #версия Python: 3.9
"""
import random

N = 10
A = [random.randint(0, 100) for i in range(N)]

print(A)
print("Max =", max(A))
