import webbrowser as wb
import sys as sy
from time import sleep

print('你的标签库')
print('登录不输入进入默认账户')
sss = input()
path = ''
if sss == '':
    print('登录成功')
    path = './tab.txt'
elif sss == 'mafengprivate':
    ssss = input()
    if ssss == 'iakcsp':
        print('登陆成功')
        path = './private.txt'
    else:
        sy.exit()
else:
    sy.exit()
try:
    fp = open(path, mode = 'r+')
except OSError as e:
    print('ERR 101:', e)
else:
    ls = fp.readlines()

    tabdic = dict()
    cnt = 0
    for s in ls:
        cnt += 1
        lss = s.split(' ')
        tabdic[lss[0]] = lss[1]
        print(lss[0], end='\n' if cnt % 4 == 0 else '   ')
    print()
    while True:
        print('打开输入open <key> 写入 write <key> <url> 其他退出')
        s = input()
        try:
            if s[:5] == 'open ':
                try:
                    wb.open_new(tabdic[s[5:]])
                except KeyError as e:
                    print('ERR 201:', e)
                    break
            elif s[:6] == 'write ':
                ll = s[6:].split(' ')
                try:
                    tabdic[ll[0]] = ll[1]
                    fp.write(ll[0] + ' ' + ll[1] + '\n')
                except KeyError as e:
                    print('ERR 401', e)
                    break
                except Exception as e:
                    print('ERR 402', e)
                    break
            else:
                fp.close()
                break
        except Exception as e:
            print('ERR 301', e)
            break
sleep(5)
