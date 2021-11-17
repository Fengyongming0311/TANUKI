#coding:utf-8
dic = dict()

dic["专辑"] = "依然范特西"

dic.setdefault("jay", "周杰伦")

dic.setdefault("中央广播电视台", "CCTV5")
#setdefault 设定默认值，设定完默认值后这个值不能做更改


print (dic)


print (dic['jay2021'])            #如果key不存在程序会报错
#上边用法，当你确定这个key是没问题的时候
print (dic.get('jay2024'))         #如果key不存在 返回None
#当不确定 你的key时候用dic.get()