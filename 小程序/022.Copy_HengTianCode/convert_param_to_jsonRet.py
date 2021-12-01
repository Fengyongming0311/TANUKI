#coding:utf-8
import tanuki

def convert_param_to_jsonRet(param):
	"""
	将A=b&c=D形式转换为dict
	:param param:
	:return:
	"""
	param = param.split('&')
	ret = {}
	for item in param:
		tmp = item.split('=')
		ret[tmp[0]]=tmp[1]
	return ret