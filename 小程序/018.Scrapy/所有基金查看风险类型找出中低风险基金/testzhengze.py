#coding:utf-8
import tanuki
import re
"""
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match() 就返回 none。
re.search 扫描整个字符串并返回第一个成功的匹配。
"""
all = "</div><table><tr><td>基金类型：<a href=\"http://fund.eastmoney.com/HH_jzzzl.html#os_0;isall_0;ft_;pt_3\">混合型-灵活</a>&nbsp;&nbsp;|&nbsp;&nbsp;高风险</td><td><a href=\"http://fundf10.eastmoney.com/gmbd_000689.html\">"

#a = re.search(r"(.*)",all)
#a = re.search("([无低中高]+风险)",all)
#print (a.group())
#tanuki.printtype(all)
#print ("-------------------------------------------------------")
#tanuki.printtype(a)

#(低|中|中低|中高|高)风险
#[低中高]+风险
#<title>.*?</title>


name = "<title>天弘添利债券(LOF)C(164206)基金净值_估值_行情走势—天天基金网</title>"

code = re.search("\([0-9]+\)", name)

fundname,shit = name.split(code.group())

code = code.group().strip("(").strip(")")

fundname = fundname.strip("<title>")
print (code)
print (fundname)