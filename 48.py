"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 48.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 48.
 #������ Python: 3.9
"""
import random

N = int(input("���������� ��������� � �������"))
A = [random.randint(-2, 2) for i in range(0, N)]

print(A)

for i in range(N):
    if A[i] == 0:
        A[i] = A[i-1] + A[i-2]
        
print(A)
