import requests, json
import urllib3
from fake_useragent import UserAgent

ua = UserAgent()
# urllib3.disable_warnings()
url = "http://172.16.1.44:8080/village/vip/list/1"
headers = {'Accept': '*/*',
           'Accept-Language': 'en-US,en;q=0.8',
           'Cache-Control': 'max-age=0',
           'User-Agent': ua.random,
           'Connection': 'keep-alive',
           'Referer': 'http://www.baidu.com/'
           }

'''
headers���壺
Accept:�ͻ��˿�ʶ������������б�
Accept-Language: ������ϣ�����õ����Ի��������
Cache-Control:���ƻ���
User-Agent:������������������
Connection:keep-alive���ֳ����ӣ�closeΪ��ϣ��ʹ�ó�����
Referer: ������Դ
:
:
'''