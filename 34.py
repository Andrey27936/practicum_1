"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 34.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 34.
 #������ Python: 3.9
"""
import random

N = int(input("������� ���������� ��������� ������� "))
a = [random.randint(0, 100) for i in range(0, N)]
print(a)
for i in range(len(a) // 2):
    a[i], a[i + len(a) // 2] = a[i + len(a) // 2], a[i]
    
print(a)
