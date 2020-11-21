"""
使用这个文件可以直接在本机生成Allure报告，前提是本机安装了allure的java版本，并且配置好了环境变量
"""
import pytest
import sys,os
#sys.path.append("..")

# path1 = sys.path.abspath(".")
#sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


if __name__ == '__main__':
    print(sys.path)
    pytest.main(["pytest/start_001_Myself_tv_Setting.py","-s", "-q", "--alluredir", "/Report/xml"])