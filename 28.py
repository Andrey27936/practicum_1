"""
 Имя проекта: practicum_1
 Номер версии: 1.0
 Имя файла: 28.ру
 Автор: 2020 © А.И. Баскаков, Челябинск
 Лицензия использования: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 Дата создания: 16/12/2020
 Описание: Задача 28.
 #версия Python: 3.9
"""
v = int(input("Скорость автомобиля:"))
t = int(input("Температура на улице:"))
if (v > 80 and t<=0) or (v > 60 and t <= -10):
    print("Езжай аккуратнее, гололед")
    v = v / 2
    print("Рекомендуемая скорость езды:", v)
elif (v > 120 and t>=30) or (v > 100 and t >= 45):
    print("Едь медленее, машина может заглохнуть")
    v = v / 3
    print("Рекомендуемая скорость езды:", v)
else:
    print("Условия для езды нормальные, едь как хочешь")
