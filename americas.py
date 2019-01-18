# -*- coding:utf-8 -*-
# 模块有更新，和书中不同
import pygal
wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'qy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file('americas.svg')
