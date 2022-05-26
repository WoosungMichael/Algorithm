N, K = map(int, input().split())
arr = list(map(int, input().split()))

diff = []
for i in range(len(arr) - 1):
    diff.append(arr[i + 1] - arr[i])

diff.sort(reverse = True)

diff = diff[K - 1:]
print(sum(diff))



# from itertools import combinations 

# N, K = map(int, input().split())
# arr = list(map(int, input().split()))

# tmp = []
# for i in range(N - 1):
#     tmp.append(i)

# check = list(combinations(tmp, K - 1))

# answer = 10000000000
# for i in check:
#     start = arr[0]
#     tmp = 0
#     for j in i:
#         end = arr[j]
#         tmp += end - start
#         start = arr[j + 1]
#     tmp += arr[-1] - start
#     if tmp < answer:
#         answer = tmp 

# print(answer)