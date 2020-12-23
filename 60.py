"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 60.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 60.
 #версия Python: 3.9
"""
import re
M = 3

list_strings = []
for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

for string in list_strings:
    string = re.sub(r'\?', '*', string)
    print(string)
