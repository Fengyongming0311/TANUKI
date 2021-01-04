#coding:utf-8
import requests
import time
from fake_useragent import UserAgent

import demjson
#通过字符串转json格式（转化为字典格式）

ua = UserAgent()




def POSTAddress(url, appkey, BankNo):
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

    quzhi = dondake['result']
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



def ReadEcxecl(url, appkey, filename):
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


        POSTAddress(url, appkey, BankCard)
        #allbankinfo.append(POSTAddress(url, appkey, BankCard))
        #将每次返回的数据插入allbankinfo列表中
        time.sleep(3)
        print ("完成---%s条---数据查询"%str(i+1))
    #return allbankinfo

def WriteExcel(filename):
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

    LastBankInfo = ReadEcxecl(filename)

    for don in LastBankInfo:
        sheet1.write(num, 0, don[0], style)  # 银行卡号
        sheet1.write(num, 1, don[1], style)  # 所属银行
        sheet1.write(num, 2, don[2], style)  # 所在城市
        sheet1.write(num, 3, don[3], style)  # 所在区县


        num = num + 1

    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    workbook.save(now + '生成银行卡结果.xls')
    print ("===================生成银行卡完成===================")



filename = "银行TEST(1).xlsx"
#这里填写要读取的Excel名称，粘贴全名进来【必须带双引号】
#WriteExcel(filename)
url = "https://api.binstd.com/bankcard/query"
#请求地址
appkey = "1e9e69716afa37e6"
#你的appkey
ReadEcxecl(url, appkey, filename)
####################################
#没有调用WriteExcel
####################################