"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 38.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 38.
 #������ Python: 3.9
"""
import array
import random

N = int(input("������� ���������� ��������� ������� "))
K = int(input("������� K "))
M = int(input("���������� ��������� ��� ��������� "))
A = [random.randint(0, 100) for i in range(0, N)]
print(A)

A.insert(K,M)
print(A)

A.delete(K,M)
