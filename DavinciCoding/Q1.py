arr = list(map(int, input().split()))

asc_cnt = 1
desc_cnt = 1

asc_tmp = 1
desc_tmp = 1

for i in range(len(arr)-1):
    if(arr[i] < arr[i+1]):
        asc_tmp += 1
        desc_tmp = 1
        if(asc_cnt < asc_tmp):
            asc_cnt = asc_tmp
    elif(arr[i] > arr[i+1]):
        desc_tmp += 1
        asc_tmp = 1
        if(desc_cnt < desc_tmp):
            desc_cnt = desc_tmp
    else:
        asc_tmp = 1
        desc_tmp = 1

print(asc_cnt, end=" ")
print(desc_cnt)
