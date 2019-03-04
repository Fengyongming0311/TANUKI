a = [1,5,7,3,6,7,33,22,111,66,7,34,8,221,74]


for i in range(len(a)):
	#print (don)
	for j in range(i,len(a)):
		if a[i] > a[j]:
			a[j],a[i] = a[i], a[j]

print (a)
	
