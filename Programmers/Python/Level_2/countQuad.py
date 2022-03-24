def divideArr(arr, x, y, d, answer):
    checkArr(arr, x, y, d // 2, answer)
    checkArr(arr, x + d // 2, y, d // 2, answer)
    checkArr(arr, x, y + d // 2, d // 2, answer)
    checkArr(arr, x + d // 2, y + d // 2, d // 2, answer)

def checkArr(arr, x, y, d, answer):
    tmp = arr[x][y]
    if d == 1:
        answer[tmp] += 1
    else:
        flag = False
        for i in range(d):
            for j in range(d):
                if arr[x + i][y + j] != tmp:
                    divideArr(arr, x, y, d, answer)
                    flag = True
                    break
            if flag:
                break
        if not flag:
            answer[tmp] += 1

def solution(arr):
    answer = [0, 0]
    checkArr(arr, 0, 0, len(arr), answer)
    
    return answer