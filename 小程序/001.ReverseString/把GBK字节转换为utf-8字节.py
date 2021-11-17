
#encode 是编码
#decode 是解码


"""s = "周杰伦"
bs1 = s.encode("GBK")
bs2 = s.encode("utf-8")
print (bs1)
print (bs2)
"""

#把一个GBK字节转化成utf-8的字节
gbk = b'\xd6\xdc\xbd\xdc\xc2\xd7'

s = gbk.decode("gbk")   #解码  因为原编码就是GBK所以用GBK方式解码
print (s)

utf8 = s.encode("utf-8")  #用utf-8编码
print (utf8)
don = utf8.decode("utf-8")

print ("###################")
print (don)

"""
1. str.encode("编码")   进行编码
2. bytes.decode("编码")  进行解码
"""