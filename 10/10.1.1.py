with open('pi_digits')as file_object:
    #关键字with在不再需要访问文件后将其关闭
    #调用open()和close()来打开和关闭文件
    #read()读取全部内容
    contents=file_object.read()
    print(contents)