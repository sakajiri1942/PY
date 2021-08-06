from urllib import request

aaa = request.urlopen('https://www.yahoo.co.jp/')
hhh = aaa.read().decode()
aaa.close()

print (hhh)
