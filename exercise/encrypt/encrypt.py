FILENAME = 'my_name.txt'
ENCRYPTION_METHOD = 1


def method_1(file, num):
    ls = file.readlines()
    ls2 = []
    for i in ls:
        s = ''
        for j in i:
            s += chr(ord(j) + num)
        ls2.append(s)
    f = ''
    for i in ls2:
        f += i
    return f


# 易位
def method_2(file, group_size):
    s = file.read()
    if len(s) % group_size != 0:
        s += ' ' * (group_size - len(s) % group_size)
    groups = len(s) // group_size
    ls = []
    for i in range(group_size):
        for j in range(groups):
            ls.append(s[j * group_size + i])
    return ''.join(ls)


ext = FILENAME.rfind('.')
f1 = open(FILENAME, 'r')
f2 = open(FILENAME[:ext] + '_encrypted' + FILENAME[ext:], 'w')

if ENCRYPTION_METHOD == 1:
    f2.write(method_1(f1, 2))
elif ENCRYPTION_METHOD == 2:
    f2.write(method_2(f1, 3))
    
f1.close()
f2.close()
