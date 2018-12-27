# -*- coding: UTF-8 -*-
# continue 用于跳过当前循环，执行下一个循环
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
