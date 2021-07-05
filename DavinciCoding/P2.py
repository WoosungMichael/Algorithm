x = int(input())

cnt = 0
tmp = 30000


def action(x, tmp):
    if(x == 1):
        return 1
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


print(action(x, tmp)-1)
