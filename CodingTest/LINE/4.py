def solution(arr, brr):
    answer = 0
    for i in range(len(arr) - 1):
        if arr[i] != brr[i]:
            answer += 1
            arr[i + 1] += arr[i] - brr[i]
    return answer