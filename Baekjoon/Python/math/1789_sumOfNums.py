N = int(input())

cnt = 0
num = 1
while True:
    if N - num >= 0:
        N -= num
        num += 1
        cnt += 1
    else:
        break
    
print(cnt)
