#1����װ�ɶ��󷵻أ��Ѷ�������װ��һ������ֱ�ӷ��ظö��󼴿ɡ�ʾ����
class Result:
	def __init__(self, result1, result2, result3, result4):
		self.result1 = result1
		self.result2 = result2
		self.result3 = result3
		self.result4 = result4


def return_results(num1, num2):
	result1 = num1 + num2
	result2 = num1 - num2
	result3 = num1 * num2
	result4 = num1 / num2
	# ��װ��result����
	result = Result(result1, result2, result3, result4)
	return result


if __name__ == '__main__':
	result = return_results(13, 4)
	print(result.result1)
	print(result.result2)
	print(result.result3)
	print(result.result4)




#����Ԫ��
def return_results(num1, num2):
	result1 = num1 + num2
	result2 = num1 - num2
	result3 = num1 * num2
	result4 = num1 / num2
	return result1, result2, result3, result4


if __name__ == '__main__':
	results = return_results(13, 4)
	print(type(results))
	for result in results:
		print(result)





#�����б�
def return_results(num1, num2):
	result1 = num1 + num2
	result2 = num1 - num2
	result3 = num1 * num2
	result4 = num1 / num2
	return [result1, result2, result3, result4]


if __name__ == '__main__':
	results = return_results(13, 4)
	print(type(results))
	for result in results:
		print(result)





#�����ֵ�
def return_results(num1, num2):
	result1 = num1 + num2
	result2 = num1 - num2
	result3 = num1 * num2
	result4 = num1 / num2

	d = dict()
	d['result1'] = result1
	d['result2'] = result2
	d['result3'] = result3
	d['result4'] = result4
	return d


if __name__ == '__main__':
	result = return_results(13, 4)
	print(type(result))
	for key in result.keys():
		print(result[key])