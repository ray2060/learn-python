o = input().split(' ')
e = input().split(' ')

for i in range(len(o)):
    if o[i] != e[i]:
        print(i)
        print(o[i])
        print(e[i])
