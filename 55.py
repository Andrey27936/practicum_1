"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 55.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 55.
 #������ Python: 3.9
"""
import re
M = 3
list_strings = []

for i in range(0, M):
    print("������� ������:", end=' ')
    list_strings.append(input())
print("������� ����:", end=' ')
syllable = input()

for string in list_strings:
    string = re.sub(syllable, '', string)
    print(string)
