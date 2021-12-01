import convert_param_to_jsonRet
#coding:utf-8
import tanuki

test = "周杰伦=范特西&光良=童话&SMAP=オレンジ"

res = convert_param_to_jsonRet.convert_param_to_jsonRet(test)

tanuki.printtype(res)