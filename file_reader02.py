# -*- coding:utf-8 -*-
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    # readlines()从文件中读取每一行，并将其存储在一个列表中。

for line in lines:
    print(line.rstrip())
