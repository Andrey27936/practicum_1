"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 47.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 47.
 #������ Python: 3.9
"""
import random

N = int(input("���������� ��������� �������"))
B = int(input("������� ������� 1"))
C = int(input("������� ������� 2"))
A = [random.randint(-10, 10) for i in range(0, N)]

print(A)

C = C + 1
del A[B:C]

print(A)
