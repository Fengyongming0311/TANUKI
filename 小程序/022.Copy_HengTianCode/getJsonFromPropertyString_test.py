import getJsonFromPropertyString
#coding:utf-8
import tanuki

test = "周杰伦=范特西&光良=童话&SMAP=オレンジ"

res = getJsonFromPropertyString.getJsonFromPropertyString(test)


tanuki.printtype(res)