import pandas as pd
'''
参数解释
filename：文件路径，可以设置为绝对路径或相对路径
sep：分隔符，常用的有逗号 , 分隔、\t 分隔，默认逗号分隔，read_table默认是'\t'(也就是tab)切割数据集的
header：指定表头，即列名，默认第一行，header = None, 没有表头，全部为数据内容
encoding：文件编码方式，不设置此选项， Pandas 默认使用 UTF-8 来解码。
index_col ，指定索引对应的列为数据框的行标签，默认 Pandas 会从 0、1、2、3 做自然排序分配给各条记录。
通过names=['a','b','c']可以自己设置列标题
'''
#result = pd.read_excel('test1.xlsx')
#普通打开一个excel表
#result = pd.read_excel('2021-1月工时.xlsx',index_col= 0)
#指定第一列为行索引

#result = pd.read_excel('2021-1月工时.xlsx',sheet_name=0)
#默认读取第一个sheet，读取第2个sheet如下




print (result)