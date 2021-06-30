n = int(input())
set = []
for i in range(n):
    set.append(list(map(int, input().split())))

set = sorted(set, key=lambda x: (x[0]))

num = 0
for i in range(len(set)):
    if(num >= set[i][0]):
        num += set[i][1]

if(num == 0):
    print(-1)
else:
    print(num)
