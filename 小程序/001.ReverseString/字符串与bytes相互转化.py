bs = bytes("字符串encode将获得一个bytes对象", encoding="utf-8")
print(bs)
print (type(bs))
s2 = bytes.decode(bs)
s3 = bs.decode()
print(s2)
print(s3)