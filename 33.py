"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 33.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 33.
 #������ Python: 3.9
"""
import random

N = int(input("������� ���������� ��������� �������"))
a = [random.randint(0, 100) for i in range(0,N)]
print(a)
if (len(a) % 2 == 1):
    end = N
else:
    end = N-1
for i in range(end-1):
    a[i], a[i + 1] = a[i + 1], a[i]
    
print(a)
