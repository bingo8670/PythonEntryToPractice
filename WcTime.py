import datetime, os
wc = open('WcTime.txt', 'w')
wc.write('hello bingo.\n')
wc.close()
wc = open('WcTime.txt', 'a+')
dt = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')
wc.write(dt)
wc.close()

wc = open('WcTime.txt')
content = wc.read()
wc.close()
print(content)

