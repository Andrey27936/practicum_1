"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: Задача 1.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 13/11/2020
 Описание: Преобразовать дату в "компьютерном" представлении (системную дату) в "российский" формат, т.е. день/месяц/год (например, 17/05/2009).
 #версия Python: 3.9
"""
T="2020.11.13"
date=T.split (".")
print (date)
print (date[2] + "/" + date [1] + "/" + date[0])
