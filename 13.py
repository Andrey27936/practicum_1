"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 13.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 13.
 #версия Python: 3.9
"""
import math
D = int(input("Введите диаметр поперечного сечения:"))
A = int(input("Введите ширину квадратного бруса:"))
A = math.sqrt(2) * A
print("Диагональ бруса равна",A)
if (A <=D):
    print("Выпилить квадратный брус шириной ",A,"возможно")
else:
    print("Выпилить квадратный брус шириной ", A, "невозможно")
