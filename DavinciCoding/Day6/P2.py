n = int(input())

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    ugly[i] = min(next2, next3, next5)
if ugly[i] == next2:
    i2 += 1
    next2 = ugly[i2] * 2
if ugly[i] == next3:
    i3 += 1
    next3 = ugly[i3] * 3
if ugly[i] == next5:
    i5 += 1
    next5 = ugly[i5] * 5

print(ugly[n-1])

# x = int(input())

# cnt = 0
# tmp = 30000


# def action(x, tmp):
#     if(x == 1):
#         return 0
#     if(x % 5 == 0):
#         if(tmp > 1+action(x/5, tmp)):
#             tmp = 1+action(x/5, tmp)
#     if(x % 3 == 0):
#         if(tmp > 1+action(x/3, tmp)):
#             tmp = 1+action(x/3, tmp)
#     if(x % 2 == 0):
#         if(tmp > 1+action(x/2, tmp)):
#             tmp = 1+action(x/2, tmp)
#     if(tmp > 1+action(x-1, tmp)):
#         tmp = 1+action(x-1, tmp)

#     return tmp


# print(action(x, tmp))


'''
x = int(input())
a = [0 for _ in range(x+1)]
a[1] = 0

for i in range(2, x+1):
    a[i] = a[i-1]+1
    if i % 5 == 0:
        a[i] = min(a[i//5]+1, a[i])
    if i % 3 == 0:
        a[i] = min(a[i//3]+1, a[i])
    if i % 2 == 0:
        a[i] = min(a[i//2]+1, a[i])
print(a[x])
'''
