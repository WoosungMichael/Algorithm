N = int(input())

arr = [0 for i in range(26)]
for i in range(N):
    tmp = input()
    arr[ord(tmp[0]) - ord('a')] += 1

flag = True
for i in range(26):
    if arr[i] >= 5:
        print(chr(ord('a') + i), end = "")
        flag = False

if flag:
    print("PREDAJA")