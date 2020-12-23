"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 51.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 51.
 #версия Python: 3.9
"""
A = [A * 3 for A in 'abc']
print(A)
B = ['Hello', 'world!', 'qwe']
print(B)
list.sort(B, key=len)
print(B)

for i in range(len(B)):
    if len(B[i]) < len(B[i+1]):
        list. insert(0, '*')
        i = i + 1
        
print(B)
