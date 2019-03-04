#coding:utf-8
"""
题目为判断一个IP地址是否合法
#
#
思路：
1.先判断字符串长度 1.1.1.1 255.255.255.255 最短7位最长15位
2.用split分解字符串
"""
def ipaddress(ip):
    #1.判断字符串是否为数字或者字母，排除中文可能性
    if 7 <= len(ip) <= 15:
        pass
    else:
        return False
    #2.对分割得到的每个字符串的每个字符进行逐一判断，如果不是数字0-9，则判定为非法IP
    cd = ip.replace(".","")
    cd = list(cd)
    for i in cd:
        try:
            int(i)
            if 0 <= int(i) <= 9:
                pass
            else:
                return False
        except:
            return False
    #3.用split(".")切分成4个数字，分别判断小于255大于0
    try:
        a,b,c,d = ip.split(".")
        for k in a,b,c,d:
            if 0 <= int(k) <= 255:
                return True
            else:
                return False

    except:
        return False


while 1:
    ip = input("输入IP地址:")
    jieguo = ipaddress(ip)
    if jieguo == False:
        print ("IP地址不合法")
    else:
        print ("IP地址合法")
