1.在RIDE->Tools-〉Preferences->Importing->Pythonpath中
设置python库文件加，这样在资源文件(resource)中以（驼峰命名）
的.py文件会被自动识别为库文件，直接Library 库名(不需要扩展名)

2.在jenkins中执行用1.方法来引用类库的用例时，需要在运行
批处理时将上述路径set在PATHONPATH环境变量中。

3.在test suite内使用custom script来引用其他path，而不要
写在RIDE的run.bat中

