import convert_json_to_param

def getJsonFromPropertyString(param):#�����ڽ�key1=value1&key2=value2תΪjson��ʽ
	# import json
	# #���п��ܲ����������ת��Ϊ�������������
	# DBG("propString:" + str(propString))
	# lastChar=propString[-1::0]
	# if (lastChar == '&'):
	#     propString = propString[0::-1]
	# if(lastChar=='='):
	#     propString=propString+"''"
	# propString.replace("=&", "=''&")
	# #�����������ת��ΪjsonString
	# propString = propString.replace("=", ":")
	# propString = propString.replace("&", ",")
	# propString = "{" + propString + "}"
	# return json.dumps(propString)
	param = param.split('&')
	ret = {}
	for item in param:
		tmp = item.split('=')
		ret[tmp[0]] = tmp[1]
	return convert_json_to_param.convert_json_to_param(ret, 0)
	#return Utility.convert_json_to_param(ret, 0)