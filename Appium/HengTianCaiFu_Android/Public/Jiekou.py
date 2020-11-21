import http.client
conn = http.client.HTTPSConnection("app.haomaojf.com")
payload = "{\"contentBelong\":\"9\"}"
headers = {
    'accept-encoding': 'gzip',
    'connection': 'Keep-Alive',
    'content-length': '21',
    'content-type': 'application/json; charset=utf-8',
    'cookie': 'APPSESSIONID=dde40dab-ceda-4a17-8e96-8c7acc66d228; Domain=haomaojf.com; Path=/; HttpOnly; SameSite=Lax',
    'host': 'app.haomaojf.com',
    'jf-app-version': '3.8.0',
    'newcardlist': 'newCardList',
    'user-agent': 'okhttp/3.9.0',
    'Content-Type': 'text/plain'
}
conn.request("POST", "/app/content/frontend/getContent", payload, headers)
res = conn.getresponse()
data = res.read().decode("utf-8")
print (data)
print (type(data))
try:
    a,b = data.split("descr\":\"")

    checkpoint,delte = b.split("\",\"linkType")
    print("getContent接口返回数据为:",checkpoint)
except:
    pass