#coding:GBK
import tanuki

import convert_json_to_param

test = (('username','嘻嘻'),('passward','哈哈'))
#tanuki.printtype(test)
test2 = "将双元素元组序列或字典编码为URL查询字符串。"
#测试传入字符串不行
test3 = ["周杰伦","给我一首歌的时间","双截棍",3]
#测试传入列表不行
test4 = {"周杰伦":"范特西","光良":"童话","SMAP":"オレンジ"}
test5 = 3.115465465
c = convert_json_to_param.convert_json_to_param(test4)

tanuki.printtype(c)