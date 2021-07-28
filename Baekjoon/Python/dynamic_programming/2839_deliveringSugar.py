N = int(input())

cnt = 0


def sugar_cnt(n, cnt):
    if(n < 0):
        print(-1)
    elif(n % 5 == 0):
        print(cnt+n//5)
    else:
        n -= 3
        cnt += 1
        sugar_cnt(n, cnt)


sugar_cnt(N, cnt)

'''
N = int(input())

cnt = 0

while(N % 5 != 0 and N >= 0):
    N -= 3
    cnt += 1

if(N < 0):
    print(-1)
else:
    print(cnt+N//5)
'''
