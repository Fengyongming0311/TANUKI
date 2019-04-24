使用pyinstaller 打.exe包

pyinstaller -F 考勤数据整理2019.04.08.py

会生成   考勤数据整理2019.04.08.spec

然后需要修改的话修改.spec文件 配置
改好后运行

pyinstaller  -F  考勤数据整理2019.04.08.spec

就会生成考勤数据整理2019.04.08.exe
就可以直接使用了
