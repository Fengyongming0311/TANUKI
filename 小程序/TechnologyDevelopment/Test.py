#coding:utf-8
from fake_useragent import UserAgent


user_agent_list = UserAgent()
ua = user_agent_list.random
ub = user_agent_list.chrome
print ("ua为*******************", ua)
print ("ub为*******************", ub)