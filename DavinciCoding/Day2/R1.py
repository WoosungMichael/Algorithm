n = int(input())

arr = list(map(int, input().split()))
arr = sorted(arr)

cnt = 0
index = 0
d = 0

while(index+d < len(arr)):
    if(arr[index+d] <= d+1):  # 코드 확인 필요!!!!
        cnt += 1
        index += d+1
        d = 0
    else:
        d += 1

print(cnt)

'''
num = int(input())
val = input()
stack = val.split()
stack = list(map(int, stack))

stack.sort()
stack.reverse()
cnt = 0
i = len(stack)-1
while i >= 0:
    print(stack)
    if stack[i] == len(stack)-i:
        cnt += 1
        for j in range(len(stack)-i):
            stack.pop()
    i -= 1
print(cnt)
'''
