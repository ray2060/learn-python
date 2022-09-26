from random import choices, randint

D1 = {
    '算法':20,
    '魔方':20,
    '初等数论':20,
    '一本涂书':6,
    '英语':6,
    '日语':6,
    '音乐':6,
    '课外书':6,
    'micro:bit':5,
    '博客':5
}
D2 = {
    0:'一',
    1:'二',
    2:'三',
    3:'四',
    4:'五',
    5:'六',
    6:'日',
}

for i in range(7):
    print('星期' + D2[i] + '：', end=' ')
    ls = []
    if i < 5:
        x = 3
    else:
        x = randint(1, 2)
    while len(ls) < x:
        l = choices(list(D1.keys()), weights=list(D1.values()))
        if l[0] in ls:
            continue
        ls.extend(l)
    for j in ls:
        print(j, end='   ')
    print('')
   
