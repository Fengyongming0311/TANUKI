import random
import json


class GetBankCardNumber(object):
    def __init__(self):
        self.binNum = ""
        self.midNum = ""
        self.lastCode = ""
        self.bankCardNumber = ""


    #获取银行卡Bin码
    def getBinNum(self, useRandom = True, bankNum = '3'):
        #主要银行的银行bin号
        bankToBin = {"工商银行": "623062",
                    "中国银行": "621343",
                    "建设银行": "622676",
                    "招商银行": "410062",
                    "中信银行": "433680",
                    "光大银行": "622663",
                    "民生银行": "622622",
                    "交通银行": "621335",
                    "平安银行": "622989",
                    "农业银行": "622848"}
        if useRandom:
            print("随机生成一个银行bin号......")
            tempBank = random.sample(bankToBin.keys(), 1)[0]
            #随机获得一个银行bin号
            self.binNum = bankToBin[tempBank]
            return self.binNum, tempBank
        
        #useRandom=False
        else:
            print("请选择银行：")
            bankList = list(bankToBin.keys())
            #打印出所有银行列表
            for i in range(len(bankList)):
                print("%d.%s" % (i, bankList[i]))
            #bankNum = input()
            if len(bankNum) == 0:
                return self.getBinNum()
            elif int(bankNum) in range(len(bankList)):
                self.binNum = bankToBin[bankList[int(bankNum)]]
                return self.binNum, bankList[int(bankNum)]
            else:
                print("输入有误，请重新输入:")
                return self.getBinNum(useRandom=False)

    def getMidNum(self, useRandom=True, tempNum = 19):
        if useRandom:
            print("默认生成一个16位的银行卡")
            tempMidnum = ""
            for x in range(9):
                tempMidnum = tempMidnum + str(random.randint(0, 10))
                x = x
            self.midNum = tempMidnum
            return self.midNum
        else:
            #tempNum = input("请输入要生成银行卡位数（16或19位）：")
            if len(tempNum) == 0:
                return self.getMidNum()
            elif int(tempNum) in (16, 19):
                tempMidnum = ""
                for x in range(int(tempNum)-6-1):
                    tempMidnum = tempMidnum + str(random.randint(0, 10))
                self.midNum = tempMidnum
                return self.midNum
            else:
                print("输入有误，请重新输入:")
                return self.getMidNum(useRandom=False)

    def getLastcode(self, bankNumNoLastcode):
        sum = 0
        for i in bankNumNoLastcode[-1::-2]:
            for m in str(int(i)*2):
                sum = sum + int(m)
        for j in bankNumNoLastcode[-2::-2]:
            sum = sum + int(j)
        if sum % 10 == 0:
            self.lastCode = '0'
        else:
            self.lastCode = str(10 - sum % 10)
        return self.lastCode

    def getBankCardNumber(self, useRandom=True):
        if useRandom:
            self.getBinNum()
            self.getMidNum()

        #不随机
        else:
            self.getBinNum(useRandom=False)
            self.getMidNum(useRandom=False)



        self.getLastcode(self.binNum + self.midNum)
        self.bankCardNumber = self.binNum + self.midNum + self.lastCode
        return self.bankCardNumber
