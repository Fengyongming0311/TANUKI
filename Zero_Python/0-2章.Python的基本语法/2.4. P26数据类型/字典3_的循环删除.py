#coding:utf-8

dic = {
	"赵四": "特别能歪嘴",
	"刘能": "老，老四啊...",
	"大脚": "跟这个和那个搞对象",
	"大脑袋": "瞎折腾...",
}

#循环删除，字典中key带 大的字眼
#因为字典在for循环中不能改变字典的大小， 所以需要一个列表存放即将要删除的key然后等循环结束用另一个for循环删除
temp = []    #存放即将要删除的key
for key in dic:
	if key.startswith("大"):
		#dic.pop(key)    #RuntimeError: dictionary changed size during iteration
		temp.append(key)


for t in temp:    #循环列表，删除字典中的内容
	dic.pop(t)

print (dic)