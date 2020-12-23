"""
 ��� �������: practicum_1
 ����� ������: 1.0
 ��� �����: 53.��
 �����: 2020 � �.�. ��������, ���������
 �������� �������������: CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
 ���� ��������: 16/12/2020
 ��������: ������ 53.
 #������ Python: 3.9
"""
import re
M = 4
def get_count(str):
    vowel = 0
    consonant = 0
    str = re.sub(r'\d', '', str)
    str = re.sub(r'\W', '', str)
    i = 0
    while i < len(str):
        char = str[i]
        if char.lower() in ['a', 'e', 'i', 'o', 'u', 'y',
                            '�', '�', '�', '�', '�', '�', '�', '�', '�', '�']:
            vowel += 1
        else:
            consonant += 1

        i += 1
    return vowel, consonant
list_strings = []
for i in range(0, M):
    print("������� ������:", end=' ')
    list_strings.append(input())

for str in list_strings:
    vowel, consonant = get_count(str)
    print("� ������ %s %s ������� � %s ���������" % (str, vowel, consonant))
