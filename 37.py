"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 37.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 37.
 #������ Python: 3.9
"""
import array
import random

N = int(input("������� ���������� ��������� ������� "))
A = [random.randint(-20, 20) for i in range(0, N)]

print(A)

B = 0
cym = np.sum(A)
C = np.size(A)
for i in range(N):
    if A[i] >= 0:
        B += A[i]
(A.insert(0, B))
(A.insert(1, C))

print(A)
