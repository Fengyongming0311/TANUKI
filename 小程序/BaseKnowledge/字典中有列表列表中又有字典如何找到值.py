#${resp['data'][0]['investFavourAuditNo']}
don = {"total":1,"data":[{"investFavourAuditNo":130200,"customerNo":962170,"businessType":1,"auditOpinion":"","interviewStatus":0,"authStatus":0,"auditStatus":0,"customerName":"董分","custType":1,"identityType":"","identityNo":"","pushPri":0,"pushPub":0,"proveCompany":"趋势科技有限公司","isDelete":0,"systemSource":0,"createId":"H029829","createName":"","createTime":"2020-12-14 13:59:28","updateId":"H029829","updateName":"","updateTime":"2020-12-14 13:59:28","custNo1":"","pubNo":"55018","totalAsset":0,"firstInvestment":"","investmentExperience":"","currentAccreditedInvestorType":"","auditDetails":"","investFavourType":"","investFavourValiddate":""}],"pageSize":10,"message":"请求成功","pageNum":1,"status":"0000"}


#audi_no = don[data][0]['investFavourAuditNo']这事错误的写法

audi_no =don['data'][0]['investFavourAuditNo']
#字典中的列表的第[0]个元素是字典的key：'investFavourAuditNo'

print (audi_no)
print (type(audi_no))