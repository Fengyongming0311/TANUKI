#coding:GBK
import tanuki

import convert_json_to_param

test = (('username','����'),('passward','����'))
#tanuki.printtype(test)
test2 = "��˫Ԫ��Ԫ�����л��ֵ����ΪURL��ѯ�ַ�����"
#���Դ����ַ�������
test3 = ["�ܽ���","����һ�׸��ʱ��","˫�ع�",3]
#���Դ����б���
test4 = {"�ܽ���":"������","����":"ͯ��","SMAP":"�����"}
test5 = 3.115465465
c = convert_json_to_param.convert_json_to_param(test4)

tanuki.printtype(c)