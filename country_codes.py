# -*- coding:utf-8 -*-
from pygal.maps.world import COUNTRIES
def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的锅别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    # 如果没找到指定的国家，就返回None
    return None

print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))
