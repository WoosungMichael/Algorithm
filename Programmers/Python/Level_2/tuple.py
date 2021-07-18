def solution(s):
    answer = []
    arr = list(s[2:-2].split('},{'))
    arr.sort(key=lambda x: len(x))
    tmp1 = list(arr[0])

    arr2 = []
    for i in arr:
        arr2.append(list(map(int, i.split(','))))

    for i in range(len(arr2)):
        arr2[i].sort()

    answer.append(arr2[0][0])
    for i in range(1, len(arr2)):
        flag = True
        for j in range(len(arr2[i-1])):
            if(arr2[i-1][j] != arr2[i][j]):
                answer.append(arr2[i][j])
                flag = False
                break
        if(flag):
            answer.append(arr2[i][-1])

    return answer
