"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 45.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 45.
 #������ Python: 3.9
"""
import random

N = int(input("���������� ��������� �������"))
A = [random.randint(-10,10) for i in range(0,N)]
print(A)
Ao = []
Ap = []
for i in range(N):
    if A[i] > 0:
        Ap.append(A[i])
    if A[i] < 0:
        Ao.append(A[i])
sumAo = np.sum(Ao)
sumAp = np.sum(Ap)
sumAo = abs(sumAo)
Q = (sumAo-sumAp)

print(sumAo)
print(sumAp)
print(Q)

if sumAo == sumAp:
    print("����� ������������� � ������������� ��������� ������� �����")
if sumAo > sumAp:
    A.append([Q])
if sumAp > sumAo:
    A.append([Q])
    
print(A)
