import http.client
import mimetypes
conn = http.client.HTTPSConnection("app.haomaojf.com")
payload = "{}"
headers = {
    'accept-encoding': 'gzip',
    'connection': 'Keep-Alive',
    'content-length': '2',
    'content-type': 'application/json; charset=utf-8',
    'cookie': 'APPSESSIONID=dde40dab-ceda-4a17-8e96-8c444c66d228; Domain=haomaojf.com; Path=/; HttpOnly; SameSite=Lax',
    'host': 'app.haomaojf.com',
    'jf-app-version': '3.8.0',
    'newcardlist': 'newCardList',
    'user-agent': 'okhttp/3.9.0',
    'Content-Type': 'text/plain'
}
conn.request("POST", "/app/account/getUserInfo", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))