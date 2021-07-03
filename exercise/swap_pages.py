n = 42
l = []
for i in range(1, n, 2):
    l.append(i)
for i in range(2, n + 1, 2):
    l.append(i)

def swap(l, p, q):
    print('swap page %d and page %d' % (p + 1, q + 1))
    temp = l[p]
    l[p] = l[q]
    l[q] = temp

x = 0
y = n - 1

print(l)
for i in range(20):
    print('----round %d----' % (i + 1,))
    x += 1
    y -= 1
    if i in [2, 5, 11, 18]:
        p = x
        q = n // 2 + 1
    elif i in [4, 9]:
        p = x
        q = n // 2 + 2
    elif i in [6, 13, 14]:
        p = x
        q = n // 2 + 3
    elif i in [8]:
        p = x
        q = n // 2 + 4
    elif i in [10]:
        p = x
        q = n // 2 + 5
    elif i in [12]:
        p = x
        q = n // 2 + 6
    elif i in [16]:
        p = x
        q = n // 2 - 2
    elif i in [17]:
        p = x
        q = n // 2 - 1
    else:
        p = x
        q = n // 2
    swap(l, p, q)
#    print(l)
    if i in [2, 5, 11]:
        p = n // 2 - 2
        q = y
    elif i in [4, 9]:
        p = n // 2 - 3
        q = y
    elif i in [6, 13, 14]:
        p = n // 2 - 4
        q = y
    elif i in [8]:
        p = n // 2 - 5
        q = y
    elif i in [10]:
        p = n // 2 - 6
        q = y
    elif i in [12]:
        p = n // 2 - 7
        q = y
    elif i in [16]:
        p = n // 2 + 1
        q = y
    elif i in [17]:
        p = n // 2
        q = y
    elif i in [18, 19]:
        continue
    else:
        p = n // 2 - 1
        q = y
    swap(l, p, q)
#    print(l)
print(l)
