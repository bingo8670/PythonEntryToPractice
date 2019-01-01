# -*- coding:utf-8 -*-
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        # restrip 方法用于消除多余的空白行
