N = int(input())

str = input()
num = []
for i in range(N):
    num.append(int(input()))

arr = []
answer = 0
for i in str:
    if i == "+":
        arr.append(arr.pop() + arr.pop())
    elif i == "*":
        arr.append(arr.pop() * arr.pop())
    elif i == "-":
        arr.append(- arr.pop() + arr.pop())
    elif i == "/":
        tmp = arr.pop()
        arr.append(arr.pop() / tmp)
    else:
        arr.append(num[ord(i) - 65])

print("{:.2f}".format(arr[0]))