"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 50.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 50.
 #������ Python: 3.9
"""
import random
N = int(input("���������� ��������� � ������� "))
A = [random.randint(-5, 5) for i in range(0, N)]

print(A)

S = 0
K = 0
L = 0

for i in range(N):
    if A[i]%3 == 0:
        S = S + 1
    if A[i]%2 == 0:
        K = K + 1
        L = L + A[i]
F = L/K
A.append(F)
A.insert(0,S)

print(F)
print(S)
print(A)
