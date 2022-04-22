filename = 'demo.txt'

# 。打开文件时，可指定读取模式（'r'）、
# 写入模式（'w'）、附加模式（'a'）或读写模式（'r+'）。如果省略了模式实参，Python 将以默认
# 的只读模式打开文件。
with open(filename, 'a') as file_object:
    file_object.write("\ni love pr")
