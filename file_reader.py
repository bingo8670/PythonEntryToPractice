# 关键字 with 在不再需要访问文件后将其关闭。
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
