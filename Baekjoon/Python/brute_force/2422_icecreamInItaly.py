from itertools import combinations

N, M = map(int, input().split())

arr = []
for i in range(M):
    arr.append(list(map(int, input().split())))

item = []
for i in range(N):
    item.append(i+1)

itemlist = list(combinations(item, 3))

answer = 0
# for i in itemlist:
#     flag = True
#     for j in arr:
#         if j[0] in i and j[1] in i:
#             flag = False
#             break
#     if flag:
#         answer += 1

for i in arr:
    newlist = []
    for j in itemlist:
        if i[0] not in j or i[1] not in j:
            newlist.append(j)
    itemlist = newlist

print(len(itemlist))
