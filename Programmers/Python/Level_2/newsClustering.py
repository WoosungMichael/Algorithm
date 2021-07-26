def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()

    arr1 = []
    for i in range(len(str1)-1):
        if(str1[i].isalpha() and str1[i+1].isalpha()):
            tmp = str1[i]+str1[i+1]
            arr1.append(tmp)

    arr2 = []
    for i in range(len(str2)-1):
        if(str2[i].isalpha() and str2[i+1].isalpha()):
            tmp = str2[i]+str2[i+1]
            arr2.append(tmp)

    union = list((set(arr1) | set(arr2)))
    join = list((set(arr1) & set(arr2)))

    cnt_u = 0
    cnt_j = 0
    for i in join:
        cnt_j += min(arr1.count(i), arr2.count(i))-1
    for i in union:
        cnt_u += max(arr1.count(i), arr2.count(i))-1

    if(len((set(arr1) | set(arr2))) == 0):
        answer = 65536
    else:
        answer = int(((len(join)+cnt_j)/(len(union)+cnt_u))*65536)

    return answer
