x = int(input())

cnt = 0
tmp = 30000


def action(x, tmp):
    if(x == 1):
        return 0
    if(x % 5 == 0):
        if(tmp > 1+action(x/5, tmp)):
            tmp = 1+action(x/5, tmp)
    if(x % 3 == 0):
        if(tmp > 1+action(x/3, tmp)):
            tmp = 1+action(x/3, tmp)
    if(x % 2 == 0):
        if(tmp > 1+action(x/2, tmp)):
            tmp = 1+action(x/2, tmp)
    if(tmp > 1+action(x-1, tmp)):
        tmp = 1+action(x-1, tmp)

    return tmp


print(action(x, tmp))


'''
x = int(input())
a = [0 for _ in range(x+1)]
a[1] = 0

for i in range(2, x+1):
    a[i] = a[i-1]+1
    if i % 5 == 0:
        a[i] = min(a[i//5]+1, a[i])
    if i % 3 == 0:
        a[i] = min(a[i//3]+1, a[i])
    if i % 2 == 0:
        a[i] = min(a[i//2]+1, a[i])
print(a[x])
'''
