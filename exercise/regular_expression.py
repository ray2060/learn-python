import re

pt = re.compile(r'(/\d[.]\d)')
s = '''
http://1.2.3.4
http://5.6.7.8
'''

l = pt.findall(s)
print(len(l))
for o in l:
    print(o)
    
