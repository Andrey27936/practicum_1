"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 56.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 56.
 #������ Python: 3.9
"""
import math
M = 3

list_strings = []
for i in range(0, M):
    print("������� ������:", end= ' ')
    list_strings.append(input())

for string in list_strings:
    strlen = len(string)

    if strlen % 2 != 0:
        print(string[math.ceil(strlen/2) - 1])
