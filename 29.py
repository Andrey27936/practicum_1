"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 29.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 29.
 #������ Python: 3.9
"""
X = int(input("������� ��� ��� ��������:"))

if (X % 4 == 0 and X % 100 != 0) or (X % 400 == 0):
    print("��� ������������:")
else:
    print("��� ����������")
if X % 100 == 0:
    X = X // 100
    print(X," ���")
elif X % 100 != 0:
    X = (X // 100) + 1
    print(X," ���")
