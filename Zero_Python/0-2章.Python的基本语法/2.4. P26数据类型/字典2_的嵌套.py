#coding:utf-8

wangfeng = {
	"name": "汪峰",
	"age": 18,
	"wife":{
		"name":"章子怡",
		"hobby":"演戏",
		"assistant":{
			"name":"樵夫",
			"age":19,
			"hobby":"打游戏"
		}
	},
	"children":[
		{"name":"孩儿1","age":13},
		{"name":"孩儿2","age":10},
		{"name":"孩儿3","age":8}
	]
}

#汪峰妻子助手的名字
name = wangfeng['wife']['assistant']['name']

print (name)


#给汪峰的第二个孩子加1岁
wangfeng['children'][1]['age'] = wangfeng['children'][1]['age'] + 1

print (wangfeng)