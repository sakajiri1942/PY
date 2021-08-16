import http.client

conn = http.client.HTTPSConnection("newscatcher.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "09c35d8e87msh8cf51e0f8dce97ap1d87aajsn85daff8f8a95",
    'x-rapidapi-host': "newscatcher.p.rapidapi.com"
    }

conn.request("GET", "/v1/latest_headlines?topic=news&lang=ja&media=True", headers=headers)

res = conn.getresponse()
data = res.read()


print(data.decode("unicode-escape"))