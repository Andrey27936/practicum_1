"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 36.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 36.
 #������ Python: 3.9
"""
N = int(input("������� ���������� ��������� ������� "))
M = int(input("���������� ��������� � ������"))
K = int(input("������� K"))
A = [random.randint(0, 100) for i in range(0, N)]
B = [random.randint(0, 100) for b in range(0, M)]

print(A)
print(B)

A.insert(K, B)
print(A)
