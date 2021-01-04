#coding:utf-8
import requests
import time
from fake_useragent import UserAgent

import demjson
#通过字符串转json格式（转化为字典格式）

ua = UserAgent()


#整合数据不出银行名称，重新做





def ZhengHeShuJu(url, appkey, BankNo):
    Posturl = url + "?" + "appkey=" + appkey + "&" + "bankcard=" + BankNo
    #每次请求的url地址
    alldata = []
    #每次劲来都是空列表

    payload={}
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ua.random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    response = requests.request("POST", Posturl, headers=headers, data=payload)

    res = response.text
    ##########################上边是请求接口获取所有数据#############################


    res = demjson.decode(res)
    #print(res)
    #print(type(res))

    if res['status'] == "210":
        #print (alldata)
        #是个空返回空列表所以加东西
        alldata.append(BankNo)
        alldata.append("")
        alldata.append("")
        alldata.append("")

        return alldata
    else:
        quzhi = res['result']
        #取出result的值
        bankcard = quzhi['bankcard']
        bank = quzhi['bank']
        sheng = quzhi['province']
        shi = quzhi['city']
        if shi == '':
            shi = sheng

        alldata.append(bankcard)
        alldata.append(bank)
        alldata.append(sheng)
        alldata.append(shi)

        return alldata




#这个是guabu
def GuaBu(url,BankNo):
    qingqiuurl = url + BankNo
    #每次请求的url地址
    alldata = []
    #每次劲来都是空列表
    liuyifandabian = "-"

    payload={}
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ua.random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    response = requests.request("GET", qingqiuurl, headers=headers, data=payload)

    a = response.text
    ##########################上边是请求接口获取所有数据#############################

    lift = "<a href=http://www.guabu.com/bank/card/%s.htm>"%BankNo

    right = "银行客服电话"

    b, c = a.split(lift)
    #C 出来了是要的内容

    d, e = c.split(right)
    #d 是要的

    """
    福建省 - 厦门</a></td></tr><tr><td height="30" align="right">银行卡种类：</td><td>中国银行 - 个人普卡 - 借记卡</td></tr><tr><td height="30" align="right">
    """
    liuyifanlaji = "</a></td></tr><tr>"

    guishudi,laji = d.split(liuyifanlaji)

    #print ("银行卡归属地为=============-------------->",guishudi)
    sheng, shi = guishudi.split(liuyifandabian)
    sheng = sheng.replace(" ", "")
    shi = shi.replace(" ", "")
    alldata.append(sheng)
    alldata.append(shi)
    #插入省市
    ##########################上边是获取银行卡归属地#############################

    liuyifanlese = "</td><td>"

    laji2, needstr = d.split(liuyifanlese)

    liuyifanchouhuo = "</td></tr><tr>"

    WhatCard,laji3 = needstr.split(liuyifanchouhuo)
    #建设银行 - 借记卡 - 龙卡通
    kazhong = dataclean(WhatCard,liuyifandabian, 1)

    #print("银行卡卡种为==============------------->",kazhong)

    alldata.insert(0,kazhong)

    alldata.insert(0,BankNo)


    ##########################上边是获取卡种#############################


    return alldata

def dataclean(shuju,fengefu,usedata):
    try:
        data1, data2 ,data3, data4 = shuju.split(fengefu)
        data1 = data1.replace(" ", "")
        data2 = data2.replace(" ", "")
        data3 = data3.replace(" ", "")
        data4 = data4.replace(" ", "")
        if usedata == 1 or usedata == "":
            return data1
        elif usedata == 2:
            return data2
        elif usedata == 3:
            return data3
        else:
            return data4
    except:
        try:
            bug1, bug2 ,bug3 = shuju.split(fengefu)
            bug1 = bug1.replace(" ", "")
            bug2 = bug2.replace(" ", "")
            bug3 = bug3.replace(" ", "")

            if usedata == 1 or usedata == "":
                return bug1
            elif usedata == 2:
                return bug2
            else:
                return bug3
        except:
            try:
                left, right = shuju.split(fengefu)
                left = left.replace(" ", "")
                right = right.replace(" ", "")
                if usedata == "" or usedata == 1:
                    return left
                else:
                    return right
            except:
                return shuju










def ReadEcxecl(ZHSJurl, GuaBuurl, appkey, filename):
    allbankinfo = []
    #银行卡号从excel读取，然后传入查询
    import xlrd

    data = xlrd.open_workbook(filename, encoding_override = 'GBK')
    #打开文件，用UTF-8格式解码,出了问题换GBK

    biao1 = data.sheet_by_index(0)
    #默认选择第一个表作为数据表

    nrows = biao1.nrows	#获取表中共有多少行数据（横行）

    for i in range(nrows):
        dondake = biao1.row_values(i)
        BankCard = str(dondake[0])
        #如果BankCard位数(小于19)用进制数据,等于19用guabu
        if len(BankCard) < 19:
            print ("BankCard小于19位------>",BankCard)
            allbankinfo.append(ZhengHeShuJu(ZHSJurl, appkey, BankCard))
            #整合数据
        else:
            allbankinfo.append(GuaBu(GuaBuurl, BankCard))
            #使用guabu网直接获取
        time.sleep(3)
        print ("完成---%s条---数据查询"%str(i+1))

    return allbankinfo
    #最后把所有列表返回






def WriteExcel(LastBankInfo):
    #加入写Excel
    import xlwt
    workbook = xlwt.Workbook() #注意Workbook的开头W要大写
    sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok = True)
    #cell_overwrite_ok参数用于确认同一个cell单元是否可以重设值。
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = 'SimSun'    # 指定“宋体”
    font.height = 230
    style.font = font
    #上设置字体
    borders = xlwt.Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1
    borders.bottom_colour = 0x3A
    style.borders = borders
    #上设置框线

    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER    #水平居中
    alignment.vert = xlwt.Alignment.VERT_CENTER    #垂直居中
    style.alignment = alignment
    #设置字体居中
    first_col = sheet1.col(0)
    first_col.width = 350 * 20

    second_col = sheet1.col(1)
    second_col.width = 270 * 20

    third_col = sheet1.col(2)
    third_col.width = 270 * 20

    fourth_col = sheet1.col(3)
    fourth_col.width = 270 * 20

    fifth_col = sheet1.col(4)
    fifth_col.width = 270 * 20

    sixth_col = sheet1.col(5)
    sixth_col.width = 270 * 20

    seventh_col = sheet1.col(6)
    seventh_col.width = 270 * 20

    seventh_col = sheet1.col(7)
    seventh_col.width = 270 * 20

    seventh_col = sheet1.col(8)
    seventh_col.width = 270 * 20

    #上设置横行的长度

    ################设置第一行字体的格式###############
    geshi = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = 'SimSun'    # 指定“宋体”
    font.height = 350
    font.bold = 'on'
    geshi.font = font
    #上设置字体
    borders = xlwt.Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1
    borders.bottom_colour = 0x3A
    geshi.borders = borders
    ##############设置第一行字体的格式完成#############

    sheet1.write(0, 0, '银行卡号', geshi)
    sheet1.write(0, 1, '所属银行', geshi)
    sheet1.write(0, 2, '所在城市', geshi)
    sheet1.write(0, 3, '所在区县', geshi)

    num = 1

    for don in LastBankInfo:
        sheet1.write(num, 0, don[0], style)  # 银行卡号
        sheet1.write(num, 1, don[1], style)  # 所属银行
        sheet1.write(num, 2, don[2], style)  # 所在城市
        sheet1.write(num, 3, don[3], style)  # 所在区县


        num = num + 1

    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    workbook.save(now + '生成银行卡结果.xls')
    print ("===================生成银行卡完成===================")









filename = "校验银行卡信息.xlsx"
#这里填写要读取的Excel名称，粘贴全名进来【必须带双引号】
#WriteExcel(filename)
ZHSJurl = "https://api.binstd.com/bankcard/query"

GuaBuurl= "http://www.guabu.com/bank/?cardid="
#请求地址
appkey = "1e9e69716afa37e6"
#你的appkey




LastBankInfo = ReadEcxecl(ZHSJurl, GuaBuurl, appkey, filename)
#查询完的值返回到这里，然后下一步再生成excel
print (LastBankInfo)
WriteExcel(LastBankInfo)
#这里生成excel