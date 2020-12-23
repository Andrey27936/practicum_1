"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 7.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 7.
 #версия Python: 3.9
"""
import random
A= random.randint (1,100)
print("Число:" + str(A))
if A % 2 == 0:
    print ("Число четное")
if A % 4 == 0:
    print ("Число кратно 4")
