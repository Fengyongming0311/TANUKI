#coding:utf-8

import requests,json
import urllib3
#urllib3.disable_warnings()
url="http://172.16.1.44:8080/sms/login"
headers={'Content-Type':'application/json;charset=UTF-8'}

request_param={
    "phoneNum":"13466738904",
	"code":"8385",
	"villageId":"1",
	"thirdId":"owY0_5VbMYzyyDsI3BtBrKGTdnfw"
}

requests.packages.urllib3.disable_warnings()
response = requests.post(url, data=json.dumps(request_param), headers=headers, verify=False)
print (response.text)