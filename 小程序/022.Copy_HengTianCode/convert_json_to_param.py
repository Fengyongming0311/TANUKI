#coding:utf-8
"""
将元组和字典 转化为 urlcode，不将汉字转码，如需要转码搭配转码使用

传入字符串，列表,int,float  不行，转化不了

"""
def convert_json_to_param(query, doseq = 0):
	import sys
	"""Encode a sequence of two-element tuples or dictionary into a URL query string.

	If any values in the query arg are sequences and doseq is true, each
	sequence element is converted to a separate parameter.

	If the query arg is a sequence of two-element tuples, the order of the
	parameters in the output will match the order of parameters in the
	input.  从urlencode粘贴过来 去掉了对于汉字的转码
	"""

	if hasattr(query, "items"):
		# mapping objects
		query = query.items()
	else:
		# it's a bother at times that strings and string-like objects are
		# sequences...
		try:
			# non-sequence items should not work with len()
			# non-empty strings will fail this
			if len(query) and not isinstance(query[0], tuple):
				raise TypeError
				# zero-length sequences of all types will get here and succeed,
				# but that's a minor nit - since the original implementation
				# allowed empty dicts that type of behavior probably should be
				# preserved for consistency
		except TypeError:
			ty, va, tb = sys.exc_info()
			raise TypeError("not a valid non-string sequence or mapping object",tb)

	l = []
	if not doseq:
		# preserve old behavior
		for k, v in query:
			k = str(k)
			v = str(v)
			l.append(k + '=' + v)
	else:
		for k, v in query:
			k = str(k)
			if isinstance(v, str):
				v = v
				l.append(k + '=' + v)
			else:
				try:
					# is this a sufficient test for sequence-ness?
					len(v)
				except TypeError:
					# not a sequence
					v = str(v)
					l.append(k + '=' + v)
				else:
					# loop over the sequence
					for elt in v:
						l.append(k + '=' + str(elt))
	return '&'.join(l)