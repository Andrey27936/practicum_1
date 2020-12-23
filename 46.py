"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 46.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 46.
 #������ Python: 3.9
"""
import random

N = int(input("���������� ��������� �������"))
T = int(input("������������� �����"))
A = [random.randint(-10, 10) for i in range(0, N)]

print(A)

S = 0
for i in range(N):
    if A[i] > 0:
        S = S + A[i]
K = T/S
for i in range(N):
    if A[i] > 0:
        A[i] += (A[i]*K)
        
print(K)
print(A)
