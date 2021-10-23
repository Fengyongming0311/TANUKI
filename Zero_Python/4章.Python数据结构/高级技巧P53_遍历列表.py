list = [["apple", "banana"], ["grape", "orange"],["watermelon"],["grapefruit"]]
#print (len(list))

for i in range(len(list)):
    print ("list[%d] :"  %i,  "",)
    for j in range(len(list[i])):
        print (list[i][j], "" ,)
        #print (i)
        #print (list[i])
        #print (j)

    print ()