num = int(input())
list = []
for i in range(num):
    list.append(int(input()))

print(max(list)-min(list))
