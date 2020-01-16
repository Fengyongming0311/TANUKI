#coding:utf-8

import requests,json
import urllib3
#urllib3.disable_warnings()
url="http://172.16.1.44:8080/sms/send"
headers={'Content-Type':'application/json'}

request_param={
    'phoneNum':'13466738904',
    'verifyCode':'0000',
    'wxOpenid':'owY0_5VbMYzyyDsI3BtBrKGTdnfw',
    'purpose':'1'
}

requests.packages.urllib3.disable_warnings()
response = requests.post(url, data=json.dumps(request_param), headers=headers, verify=False)
print (response.text)