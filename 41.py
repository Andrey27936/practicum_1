"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 41.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 41.
 #������ Python: 3.9
"""
import random

N = int(input("���������� ��������� �������"))
A = [1,5,3,-4]

print(A)

a = 0
for i in range(N):
    if A[i] >= 0:
        break
    if A[i] < 0:
        for i in range(N):
            if A[i-1] < A[i]:
                a = 0
            else:
                a =1
                break
        A[i] = A[i] - 1
        
if (a == 0):
    print("������������")
    
else:
    print("���������")
