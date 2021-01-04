#coding:utf-8
"""
字典中有列表然后又有字典，如何取出想要的值
"""
dondake  =  {"data":[{"fixPriceId":"DJ20201221007","priceMeetingDate":"2020-12-21","fixPriceRemark":"定价会新增","realProductId":36536,"priceResults":1,"priceResultsMemo":"","channelManageRate":"","channelPerformPate":"","managePerformRate":"","managePerformStan":"","performCoefficient":"","annualizedBaseDay":"","equitiesCoefficient":1.00,"effectiveDate":"","specialFareMemo":"","payMode":"","postPointLocation":"","auditState":1,"discardReason":"","createId":"H029829","createName":"冯泳铭","createTime":"2020-12-21 16:03:16","updateId":"","updateName":"","updateTime":"2020-12-21 16:03:16","productCode":"CP20201221015","productName":"萨拉热窝的罗密欧与朱丽叶募集期产品202012211530","productType":3,"incomeType":0,"shortName":"","currency":"","term":"","termUnit":"","auditCreateTime":"","branchName":"","incomeAccountingType":"","balePrice":""}],"status":"0000","message":"查询成功","pages":1,"pageNum":1,"pageSize":10,"total":1,"params":{}}


#print (dondake)
#print (type(dondake))

a = dondake['data']
#print (dondake['data'])
#print (a)
#print (type(a))


don = a[0]

#print (don)
#print (type(don))


tanuki = don['fixPriceId']


print (tanuki)
print (type(tanuki))