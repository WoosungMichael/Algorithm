N = int(input())

num = 1
for i in range(N):
    num *= (i+1)

num = str(num)[::-1]

for i in num:
    if i != '0':
        print(i)
        break