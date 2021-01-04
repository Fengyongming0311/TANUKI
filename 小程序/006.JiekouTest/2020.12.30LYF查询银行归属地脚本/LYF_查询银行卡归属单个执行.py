import requests
import re




def BankCardAddress(url):

    payload={}
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    a = response.text

    lift = "<a href=http://www.guabu.com/bank/card/%s.htm>"%BankCard

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

    liuyifanlese = "</td><td>"

    laji2, needstr = d.split(liuyifanlese)

    liuyifanchouhuo = "</td></tr><tr>"

    kazhong,laji3 = needstr.split(liuyifanchouhuo)

    #print("银行卡卡种为==============------------->",kazhong)


    liuyifanzhazha = "-"









    alldata = yinhang + "," + sheng + "," + shi

    return alldata



def dataclean(shuju,fengefu,usedata):
    try:
        left, right = shuju.split(fengefu)

        if usedata == "" or usedata == 1:
            return left
        else:
            return right
    except:
        data1, data2 ,data3 = shuju.split(fengefu)










#BankCard = input("请输入你要查询的银行卡：")

BankCard = "6217003480004505843"

#print("银行卡号为=============---------->",BankCard)


url = "http://www.guabu.com/bank/?cardid="+BankCard

print(BankCardAddress(url))