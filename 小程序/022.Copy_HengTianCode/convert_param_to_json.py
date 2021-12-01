#coding:utf-8
def convert_param_to_json(param):
	"""
	 将A=b&c=D形式转换为 jsonString
	 代码中另一个返回值为ret，出BUG时候可以替换试试
	:param param:
	:return:
	"""
	param = param.split('&')
	ret = {}
	for item in param:
		tmp = item.split('=')
		ret[tmp[0]]=tmp[1]
	#return str(ret).replace("u'",'"').replace("'",'"')
	#return ret