"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 39.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 39.
 #������ Python: 3.9
"""
import random

N = int(input("������� ���������� ��������� ������� "))
A = [random.randint(-1, 1) for i in range(0, N)]

print(A)
B = filter(bool, A)
print(list(B))
