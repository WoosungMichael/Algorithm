def solution(arr):
    answer = 0
    arr.sort()
    if len(arr)==1:
        answer = arr[0]
    else:
        n = 1
        while True:
            flag = True
            for i in range(len(arr)-1):
                if (arr[-1]*n)%arr[i] != 0:
                    flag = False
                    break
            if flag:
                answer=arr[-1]*n
                break
            n+=1
    return answer