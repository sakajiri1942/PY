from urllib import request

response = request.urlopen('https://www.pasonatech.co.jp/')
content = response.readlines()
response.close()


print(content)