"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 31.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 31.
 #������ Python: 3.9
"""
import random

n = 25
a = [random.randint(0, 100) for i in range(n)]
print(a)
N = 1
while N < n - 1:
    for i in range(n - N):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    N += 1
    
print(a)
