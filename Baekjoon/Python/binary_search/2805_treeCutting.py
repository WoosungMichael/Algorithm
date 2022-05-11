N, M = map(int, input().split())
arr = list(map(int, input().split()))

d, u = 0, max(arr)
while d < u:
    cut = (d + u) // 2
    sum = 0
    for i in arr:
        sum += max(i - cut, 0)
    if sum >= M:
        if d == cut:
            break
        d = cut
    else:
        if u == cut:
            break
        u = cut
    
print(cut)