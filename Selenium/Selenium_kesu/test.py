#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, time, re, os

driver = webdriver.Chrome("C:\\ProgramData\\Anaconda3\\chromedriver.exe")
driver.maximize_window()
driver.get("http://test-sso-java.seedland.cc/login?challengeNumber=eG9vdTRuOTlkdHgxN3N2aWxuZHJybjRnZG1xNTRmbm94Y2V0dnhicW4zM3AxOGx2bzc5c25ncWl0eGJicmtwMGVkajQ5dTM2dDJjcmt5eXo1OGIyZmZicWs0cmNidXIyb3dyMmplbGk5NHBiaHVzcHFlaTQ0NGsydWFtMjdhbnRxc2Mza3ZtcmFlbmRqMWZsMWMycW5sOWNvaW85ZnphY25mZmRpNnI5c3R3YWZ5Z3U4bTNhcHNzOGQ2czhqNWxnejF6Z3Z4a21oZmcyZmhvdXoyMmZkbDN2aGU5YWNlb2lhN3Z2eGdqendwb2tuYWhucDZzMjRleTlvdjE5bmtiZA==&flag=3&systemCode=SSO1028&RetutnUrl=http%3A%2F%2Fasm-test.seedland.cc%3A8082%2Flife-web%2FleadershipKanban%2FnewLeadershipKanbanJsp")
driver.implicitly_wait(30)
#####################

#登录
driver.find_element_by_css_selector('input[name=\"txtUserName\"]').send_keys("aiwensi")
#<input name="txtUserName" onblur="tokenisext();" id="txtUserName" maxlength="30" type="text" value="" placeholder="用户名">
time.sleep(1)
driver.find_element_by_css_selector('input[name=\"txtPassword\"]').send_keys("1")
#<input name="txtPassword" id="txtPassword" type="password" value="" placeholder="请输入密码" maxlength="30">
time.sleep(1)
driver.find_element_by_css_selector('input[class=\"button\"]').click()
#<input class="button" id="_login" onclick="login();" type="button" value="登录">
time.sleep(1)

#进入报事管理→接待中心
driver.find_element_by_link_text("报事管理").click()
#<a href="javascript:void(0);">报事管理<span class="layui-nav-more"></span></a>
time.sleep(1)
driver.find_element_by_partial_link_text("接待中心").click()
#<a href="/life-web/life/call/centrePage?header_Identification=things&amp;hiddenRight=true" target="_blank">接待中心</a>
time.sleep(1)

allwindows = driver.window_handles

#获取所有窗口
#print (allwindows)
#print ("================================================")
nowwindow1 = driver.current_window_handle
#print ("这个应该是新页面的句柄",nowwindow1)

for smap in allwindows:
    #print(smap)
    if smap != nowwindow1:
        driver.switch_to_window(smap)

time.sleep(3)
#print ("开始定位")
#进入物业客诉
driver.find_element_by_css_selector('li[id=\"wuyeliebiao\"]').click()
#<li id="wuyeliebiao" data-url="/guestComplaint/wuye">物业客诉</li>
time.sleep(2)
#系统可能不会保存您所做的更改→点击确定
driver.find_element_by_partial_link_text("确定").click()
#<a class="layui-layer-btn0">确定</a>
time.sleep(3)

#切换iframe
driver.switch_to_frame("mainContent")
time.sleep(3)


#driver.find_element_by_css_selector('a[onclick=\"reQueryForm(\'time\',7)\"]').click()
#driver.find_element_by_link_text("最近一周").click()
driver.find_element_by_css_selector("#queryForm > div.layui-form > div > div:nth-child(6) > a").click()
#driver.find_element_by_xpath("//*[@id=\"queryForm\"]/div[1]/div/div[6]/a").click()
#driver.find_element_by_xpath("//*[@id=\"queryForm\"]/div[1]/div/div[7]/a").click()
#点击最近一周缩小范围
#<a href="javascript:;" onclick="reQueryForm('time',7)" title="点击查询">最近一周</a>
time.sleep(1)

driver.find_element_by_xpath("//*[@id=\"queryForm\"]/div[3]/div/div/div/table/tbody/tr[1]/td[1]/a[1]").click()
#找到最新的一条点击编辑
#<a href="/life-web/guestComplaint/edit/2108/wuye" onclick="setIframeHeight(false)">编辑</a>
#<a href="/life-web/guestComplaint/edit/2107/wuye" onclick="setIframeHeight(false)">编辑</a>
#<a href="/life-web/guestComplaint/edit/2111/wuye" onclick="setIframeHeight(false)">编辑</a>
#//*[@id="queryForm"]/div[3]/div/div/div/table/tbody/tr[1]/td[1]/a[1]

#driver.find_element_by_css_selector("span[data=\"2\"][class=\"appealNature\"]").click()
driver.find_element_by_xpath("//*[@id=\"reportResponsibility\"]/span[1]").click()
#<span data="2" class="appealNature">地产</span>
#进入编辑页面选择责任部门 为地产

time.sleep(1)
driver.find_element_by_xpath("//*[@id=\"submitFrom\"]/a[2]").click()
#<a onclick="saveCenter(22)" class="layui-btn">分派工单</a>
#点击分派工单

time.sleep(1)
driver.find_element_by_xpath("//*[@id=\"layui-layer1\"]/div[3]/a[1]").click()
#点击是分派工单

time.sleep(1)
driver.find_element_by_xpath("//*[@id=\"orderForm\"]/div[2]/div[1]/div[1]/div").click()
#<div class="layui-unselect layui-form-switch" lay-skin="_switch"><em>关</em><i></i></div>
#点击供应商开关，关→开
time.sleep(3)

#<span class="select2-selection__rendered" id="select2-supplier-container"><span class="select2-selection__placeholder">请选择供应商</span></span>
driver.find_element_by_xpath("//*[@id=\"select2-supplier-container\"]").click()

time.sleep(2)
#<input type="text" placeholder="请选择" value="天责任2" readonly="" class="layui-input layui-unselect">
#<li class="select2-results__option" role="treeitem" aria-selected="false">天责任2</li>
#//*[@id="select2-supplier-results"]/li[2]
driver.find_element_by_xpath("//*[@id=\"select2-supplier-results\"]/li[2]").click()