#coding:utf-8
"""
可读汉字转为杠u开头的编码
"""

a = '萨拉热窝的罗密欧与朱丽叶募集期产品202012211530'

import json



b = json.dumps(a)

print (b)
print(type(b))