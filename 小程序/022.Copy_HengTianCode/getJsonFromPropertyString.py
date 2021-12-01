import convert_json_to_param

def getJsonFromPropertyString(param):#适用于将key1=value1&key2=value2转为json格式
	# import json
	# #将有可能不规则的数据转化为规则的完整数据
	# DBG("propString:" + str(propString))
	# lastChar=propString[-1::0]
	# if (lastChar == '&'):
	#     propString = propString[0::-1]
	# if(lastChar=='='):
	#     propString=propString+"''"
	# propString.replace("=&", "=''&")
	# #将规则的数据转化为jsonString
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