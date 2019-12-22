#coding:utf-8

import requests,json
import urllib3
#urllib3.disable_warnings()
url="http://172.16.1.44:8081/village/all"
headers={'Content-Type':'application/json;charset=UTF-8',
		 "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1Nzk2NjIxMDcsImFjY291bnQiOnsiaWQiOjUzLCJ2aWxsYWdlSWQiOm51bGwsInBob25lTnVtIjoiMTM0NjY3Mzg5MDQiLCJwYXNzd29yZCI6bnVsbCwibmlja25hbWUiOiLmnYPpkasiLCJwaG90byI6Imh0dHBzOi8vd3gucWxvZ28uY24vbW1vcGVuL3ZpXzMyL0RZQUlPZ3E4M2VvTHBGcmR1dEVZMTNOTHZScnZmOUVxM1RrcXNMSnowdVlPeXZpYVp4aWJ3eTE5RzY5aWJacEhBYUtlZElsTFpuYWFEd1dZMnJ1a3RtZ1N3LzEzMiIsInNleCI6bnVsbCwicmVnaXN0ZXJEYXRlIjoxNTc2OTEzMTExMDAwLCJmaXJzdExvZ2luVGltZSI6MTU3NjkxMzExMTAwMCwibGFzdExvZ2luVGltZSI6MTU3NjkyODU3NjAwMCwid3hPcGVuSWQiOiJvd1kwXzVWYk1Zenl5RHNJM0J0QnJLR1RkbmZ3IiwidG9rZW4iOiJleUowZVhBaU9pSktWMVFpTENKaGJHY2lPaUpJVXpJMU5pSjkuZXlKaFkyTnZkVzUwSWpwN0ltbGtJam8xTXl3aWRtbHNiR0ZuWlVsa0lqcHVkV3hzTENKd2FHOXVaVTUxYlNJNklqRXpORFkyTnpNNE9UQTBJaXdpY0dGemMzZHZjbVFpT201MWJHd3NJbTVwWTJ0dVlXMWxJam9pNXAyRDZaR3JJaXdpY0dodmRHOGlPaUpvZEhSd2N6b3ZMM2Q0TG5Gc2IyZHZMbU51TDIxdGIzQmxiaTkyYVY4ek1pOUVXVUZKVDJkeE9ETmxiMHh3Um5Ka2RYUkZXVEV6VGt4MlVuSjJaamxGY1ROVWEzRnpURXA2TUhWWlQzbDJhV0ZhZUdsaWQza3hPVWMyT1dsaVduQklRV0ZMWldSSmJFeGFibUZoUkhkWFdUSnlkV3QwYldkVGR5OHhNeklpTENKelpYZ2lPbTUxYkd3c0luSmxaMmx6ZEdWeVJHRjBaU0k2TVRVM05qa3hNekV4TVRBd01Dd2labWx5YzNSTWIyZHBibFJwYldVaU9qRTFOelk1TVRNeE1URXdNREFzSW14aGMzUk1iMmRwYmxScGJXVWlPakUxTnpZNU1UTXhNVEV3TURBc0luZDRUM0JsYmtsa0lqb2liM2RaTUY4MVZtSk5XWHA1ZVVSelNUTkNkRUp5UzBkVVpHNW1keUlzSW5SdmEyVnVJam9pWlhsS01HVllRV2xQYVVwTFZqRlJhVXhEU21oaVIyTnBUMmxLU1ZWNlNURk9hVW81TG1WNVNtaFpNazUyWkZjMU1FbHFjRGRKYld4clNXcHZNVTE1ZDJsa2JXeHpZa2RHYmxwVmJHdEphbkIxWkZkNGMweERTbmRoUnpsMVdsVTFNV0pUU1RaSmFrVjZUa1JaTWs1NlRUUlBWRUV3U1dsM2FXTkhSbnBqTTJSMlkyMVJhVTl0TlRGaVIzZHpTVzAxY0ZreWRIVlpWekZzU1dwdmFUVndNa1EyV2tkeVNXbDNhV05IYUhaa1J6aHBUMmxLYjJSSVVuZGplbTkyVEROa05FeHVSbk5pTW1SMlRHMU9kVXd5TVhSaU0wSnNZbWs1TW1GV09IcE5hVGxGVjFWR1NsUXlaSGhQUkU1c1lqQjRkMUp1U210a1dGSkdWMVJGZWxScmVESlZia295V21wc1JtTlVUbFZoTTBaNlZFVndOazFJVmxwVU0yd3lZVmRHWVdWSGJHbGtNMnQ0VDFWak1rOVhiR2xYYmtKSlVWZEdURnBYVWtwaVJYaGhZbTFHYUZKSVpGaFhWRXA1WkZkME1HSlhaRlJrZVRoNFRYcEphVXhEU25wYVdHZHBUMjAxTVdKSGQzTkpia3BzV2pKc2VtUkhWbmxTUjBZd1dsTkpOazFVVlROT2FtdDRUWHBGZUUxRWEzbFBRM2RwV20xc2VXTXpVazFpTW1Sd1lteFNjR0pYVldsUGFrVXhUbnBaTlUxVVRYaE5WRUUxVFdwbmMwbHRlR2hqTTFKTllqSmtjR0pzVW5CaVYxVnBUMnBGTVU1NldUVk5WRTE0VFZSQk5VMXFaM05KYm1RMFZETkNiR0pyYkd0SmFtOXBZak5rV2sxR09ERldiVXBPVjFod05XVlZVbnBUVkU1RFpFVktlVk13WkZWYVJ6VnRaSGxKYzBsdVVuWmhNbFoxU1dwd2RXUlhlSE5NUTBwcVkyMVdhR1JIVmtWWldGSnNTV3B3ZFdSWGVITk1RMG94WTBkU2FHUkhWa1ZaV0ZKc1NXcHdkV1JYZUhOTVEwcHdZekJTYkdKSFZqQmFVMGsyWW01V2MySkRkMmxaTTBwc1dWaFNiRkZ1YTJsUGJUVXhZa2QzYzBsdVZuZGFSMFl3V2xWS05VbHFjSFZrVjNoelpsZ3dMbDlLTW5welZtTjVZbWN5TFRCRmVHeHRSR2hUUjBoUWN6RTJURjlFZGpkcVMyODNOaTE1ZFdoYU4xa2lMQ0pqY21WaGRHVkVZWFJsSWpwdWRXeHNMQ0oxY0dSaGRHVkVZWFJsSWpwdWRXeHNMQ0pwYzBSbGJHVjBaU0k2Ym5Wc2JDd2lZM0psWVhSbFFua2lPbTUxYkd3c0luVndaR0YwWlVKNUlqcHVkV3hzZlgwLkEtMnBWZWg0dnowUkVubGUzYmpCLTZQQk5pUHo0Tm1FTkxJeEFoOHp3Zm8iLCJjcmVhdGVEYXRlIjpudWxsLCJ1cGRhdGVEYXRlIjpudWxsLCJpc0RlbGV0ZSI6bnVsbCwiY3JlYXRlQnkiOm51bGwsInVwZGF0ZUJ5IjpudWxsfSwibmJmIjoxNTc2OTgzNzA3fQ.BWQCbA1ZusEjM0v8mqK_KvqlZS9RkYqOrV4u4540mPI"}

request_param={
    "phoneNum":"13466738904",
	"code":"8385",
	"villageId":"1",
	"thirdId":"owY0_5VbMYzyyDsI3BtBrKGTdnfw"
}

requests.packages.urllib3.disable_warnings()
response = requests.get(url, headers=headers, verify=False)
print (response.text)