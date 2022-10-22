import webbrowser as wb
import re
import requests as rq

print('AcWing题库acw，Luogu题库lg')
st = input('输入要打开的题号或题目名（洛谷暂只支持题号），每个题号之间用英文半角逗号分开')
problem_list = st.split(',')

for s in problem_list:
    if s[:2] == 'lg':
        try:
            wb.open_new('https://www.luogu.com.cn/problem/' + s[2:])
        except Exception as e:
            print('ERR')
            print(s)
            print(e)
    if s[:3] == 'acw':
        try:
            rqgot = rq.get('https://www.acwing.com/problem/search/1/?csrfmiddlewaretoken=U3X9aMa8s4VCPxVfNtobZ1MKEKnwkb9dhAqt7UjpqDoLBG0oezzzXWm54gmRPTO2&search_content=' + s[3:])
            rqtxt = rqgot.text
            x = re.search('content[/]\d+', rqtxt).span()
            start = x[0] + 8
            z = ''
            for i in range(start, x[1]):
                c = rqtxt[i]
                if c in ['0','1','2','3','4','5','6','7','8','9']:
                    z += c
                else:
                    break;
            wb.open_new('https://www.acwing.com/problem/content/' + z + '/')
        except Exception as e:
            print('ERR')
            print(s)
            print(e)
