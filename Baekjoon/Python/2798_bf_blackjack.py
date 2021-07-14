from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))

card_list = list(combinations(arr, 3))
max = 0
for i in card_list:
    if(sum(i) <= M and sum(i) > max):
        max = sum(i)

print(max)
