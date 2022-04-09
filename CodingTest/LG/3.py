def solution(letters, k):
    answer = ''
    cnt = 0
    start = 0
    while True:
        max_index = start
        for i in range(start, len(letters) - k + cnt + 1):
            if letters[i] == 'z':
                max_index = i
                break
            if ord(letters[max_index]) < ord(letters[i]):
                max_index = i
        answer += letters[max_index]
        start = max_index + 1
        cnt += 1
        if cnt == k:
            break

    return answer