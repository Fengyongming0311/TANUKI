使用pyinstaller 打.exe包
将需要打包的文件拷到与pyinstaller.exe 同级的文件夹中
我的是 C:\ProgramData\Anaconda3\Scripts



在 C:\ProgramData\Anaconda3\Scripts  打开CMD命令

pyinstaller -F 考勤数据整理2019.04.26.py

会生成   考勤数据整理2019.04.08.spec

然后需要修改的话修改.spec文件 配置
改好后运行

pyinstaller  -F  考勤数据整理2019.04.26.py

就会生成考勤数据整理2019.04.08.exe
就可以直接使用了
