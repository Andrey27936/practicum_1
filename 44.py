"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 44.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 44.
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
sumAo = np.size(Ao)
sumAp = np.size(Ap)
Q = sumAo-sumAp
W = sumAp - sumAo
print(sumAo)
print(sumAp)

if sumAo == sumAp:
    print("���������� ������������� � ������������� ��������� ������� �����")
if sumAo > sumAp:
    A.append([random.randint(1,10) for i in range(0,Q)])
if sumAp > sumAo:
    A.append([random.randint(-1, -10) for i in range(0,W)])
    
print(A)
