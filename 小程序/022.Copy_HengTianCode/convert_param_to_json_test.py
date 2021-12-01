#coding:utf-8
import tanuki

import convert_param_to_json

code = "周杰伦=范特西&光良=童话&SMAP=オレンジ"

re = convert_param_to_json.convert_param_to_json(code)

tanuki.printtype(re)