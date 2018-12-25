import requests
import re

def getimagelist(num=1):
    img1 = requests.get('http://www.doutula.com/photo/list/?page={}'.format(num))
    html = img1.text
    reg = r'data-original="(.+?)"'
    imglist = re.findall(reg,html)
    return imglist
print (getimagelist())
