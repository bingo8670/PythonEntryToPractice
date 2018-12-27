# -*- coding:UTF-8 -*-
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# 一条名为While 的小狗
describe_pet("willie")
describe_pet(pet_name='willie')

# 一只名为Harry 的仓鼠
describe_pet('hamster', 'harry')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


