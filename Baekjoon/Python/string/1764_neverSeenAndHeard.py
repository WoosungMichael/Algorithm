import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr1 = []
arr2 = []

for i in range(N):
    arr1.append(input().strip())
for i in range(M):
    arr2.append(input().strip())
intersection = sorted(list(set(arr1) & set(arr2)))

print(len(intersection))
for i in intersection:
    print(i)
