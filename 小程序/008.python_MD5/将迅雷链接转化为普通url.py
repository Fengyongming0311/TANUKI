# -*- coding: utf-8 -*-

import base64

from urllib.parse import unquote
def jie_ma(http_str):
	print(unquote(http_str))


def convert_2(thunder_url):
	tmp = thunder_url.replace('thunder://', '')
	http_str = base64.b64decode(tmp.encode()).decode('gbk')[2:-2]
	return http_str


if __name__ == '__main__':
	thunder_url = input("请输入迅雷链接:")
	http_str = convert_2(thunder_url)
	jie_ma(http_str)