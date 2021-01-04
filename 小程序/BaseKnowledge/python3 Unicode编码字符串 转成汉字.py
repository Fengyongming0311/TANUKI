#coding:utf-8
"""
\u8428\u62c9\u70ed\u7a9d\u7684\u7f57\u5bc6\u6b27\u4e0e\u6731
\u开头的编码转为可读汉字
"""

a = "\u8428\u62c9\u70ed\u7a9d\u7684\u7f57\u5bc6\u6b27\u4e0e\u6731\u4e3d\u53f6\u52df\u96c6\u671f\u4ea7\u54c120201221153020201222155041643"

a = a.encode("utf-8").decode("utf-8")
 
print(a)
