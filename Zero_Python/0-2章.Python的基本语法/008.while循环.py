#while循环
numbers = input("输入几个数字，用逗号分隔：").split(",")

print (numbers)

x = 0

#当x的值小于输入字数的个数的时候，执行循环内容
while x < len(numbers):
	print (numbers[x])
	x += 1