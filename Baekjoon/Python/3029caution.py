t1 = list(map(int, input().split(":")))
t2 = list(map(int, input().split(":")))
arr = []

if(t2[2]-t1[2] < 0):
    arr.append(t2[2]-t1[2]+60)
    t2[1] = t2[1]-1
else:
    arr.append(t2[2]-t1[2])

if(t2[1]-t1[1] < 0):
    arr.append(t2[1]-t1[1]+60)
    t2[0] = t2[0]-1
else:
    arr.append(t2[1]-t1[1])

if(t2[0]-t1[0] < 0):
    arr.append(t2[0]-t1[0]+24)
else:
    arr.append(t2[0]-t1[0])

arr.reverse()
for i in range(len(arr)):
    arr[i] = '{0:0>2}'.format(arr[i])
arr = list(map(str, arr))

if(arr.count('00') == 3):
    arr[0] = '24'

time = ':'.join(arr)

print(time)
