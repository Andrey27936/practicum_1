"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 43.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 43.
 #������ Python: 3.9
"""
import random

N = int(input("���������� ��������� �������"))
A = [random.randint(-10,10) for i in range(0,N)]
Ao = []
Ap = []

for i in range(N):
    if A[i] > 0:
        Ap.append(A[i])
    if A[i] < 0:
        Ao.append(A[i])
        
print("�������������",Ao)
print("�������������",Ap)
