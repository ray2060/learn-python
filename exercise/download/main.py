print("欢迎使用下载文件器1.0.0")
print('正在初始化中， 约需3秒...')
import requests
import time


while True:
	if input('下载内容？(y/n)') == 'y':
		a = True
	else:
		break
	file_name = input('文件名：')
	print('获取文件中，约需10秒...')
	res = requests.get("https://r.pythoner.work/downloads_other/" + file_name)
	if res.status_code == 404:
		print('404:(')
		continue
	if input('文件我们找到了，你要下载它吗？(y/n)') == 'y':
		b = True
	else:
		b = False
	if not b:
		continue
	path = input('存储在：')
	print('下载中， 约需15秒...')
	try:
		with open(path + file_name, 'w') as f:
			f.write(res.text)
	except:
		print('出了一点点问题:(')
		continue
	print('文件下载完毕')
print('感谢您的使用')
print('程序将在3秒后自动退出')
time.sleep(3)
