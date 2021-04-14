FILENAME = 'C:\\_mega\\_ray\\stem\\python\\exercise\\abc.txt'           # 输入位置和文件名，反斜杠\需要写两次\\

f = open(FILENAME, 'r')
print(f.read())
f.close()
