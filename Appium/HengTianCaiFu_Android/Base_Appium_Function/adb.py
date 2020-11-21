import os
class input(object):

    # 输入文字
    def text(self,text):
        adb = 'adb shell input text %s'%text
        os.popen(adb)

    # 滑动
    def swipe(self,x,y,x1,y1):
        adb = 'adb shell input swipe %s %s %s %s '%(x,y,x1,y1)
        os.popen(adb)

    # 模拟按键
    def keyevent(self,k):
        adb = 'adb shell input keyevent %s'%k
        os.popen(adb)

if __name__ == '__main__':
    adb = input()
    adb.text(1111)
    adb.swipe(280,720,280,240)
    adb.keyevent(3)