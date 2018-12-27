# -*- coding:UTF-8 -*-
def greet_user(names):
    """向列表中的每位用户都发出简单的问候语"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_user(usernames)
