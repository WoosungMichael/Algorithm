from collections import deque

N, K = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()
cnt = 0
max_cnt = 0
flag_end = False
for i in range(len(arr)):
    arr[i] %= 2
    if arr[i] == 0:
        cnt += 1
    if sum(q) + arr[i] <= K:
        q.append(arr[i])
    else:
        if cnt > max_cnt:
            max_cnt = cnt
        while sum(q) + arr[i] > K and q:
            tmp = q.popleft()
            if tmp == 0:
                cnt -= 1
        q.append(arr[i])

if cnt > max_cnt:
    max_cnt = cnt

print(max_cnt)

# from collections import deque

# N, K = map(int, input().split())
# arr = list(map(int, input().split()))

# odd = []
# odd_cnt = 0

# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         if odd_cnt != 0:
#             odd.append(odd_cnt)
#             odd_cnt = 0
#         odd.append(0)
#     else:
#         odd_cnt += 1

# q = deque()
# cnt = 0
# max_cnt = 0
# flag_end = False
# for i in range(len(odd)):
#     if odd[i] == 0:
#         cnt += 1
#     if sum(q) + odd[i] <= K:
#         q.append(odd[i])
#     else:
#         if cnt > max_cnt:
#             max_cnt = cnt
#         while sum(q) + odd[i] > K and q:
#             tmp = q.popleft()
#             if tmp == 0:
#                 cnt -= 1
#         q.append(odd[i])

# if cnt > max_cnt:
#     max_cnt = cnt

# print(max_cnt)