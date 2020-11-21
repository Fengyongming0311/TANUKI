# coding:utf-8

import requests, json
import urllib3


customer_account = []
# urllib3.disable_warnings()
url = "http://hq.sinajs.cn/list=sz002594"

requests.packages.urllib3.disable_warnings()
response = requests.get(url, verify=False)
#print("DonDaKe",response.text)
a = str(response.text)

customer_account = a.split(",")


customer_now = customer_account[3]


print ("当前中岩客户编号为：",customer_now)




customer_auth = "http://qt.gtimg.cn/q=r_hk01810"

requests.packages.urllib3.disable_warnings()
response = requests.get(customer_auth, verify=False)

don = str(response.text)

customer_contact = don.split("~")
#print (customer_contact)

zy_accredited_validdate = customer_contact[3]

print ("投资者分类查询出客户编号为：",zy_accredited_validdate)




zy_investfavour_auth = "http://qt.gtimg.cn/q=r_hk00354"

requests.packages.urllib3.disable_warnings()
response = requests.get(zy_investfavour_auth, verify=False)

don = str(response.text)

#print (don)

mobile_internet = don.split("~")
#print (mobile_internet)


zy_investfavour_validdate = mobile_internet[3]


print ("公募客户编号客户编号为：",zy_investfavour_validdate)
