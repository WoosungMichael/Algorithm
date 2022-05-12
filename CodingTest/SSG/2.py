def solution(s):
    answer = 1
    length = len(s)

    for i in range(length):
        for j in range(length - 1, i, -1):
            if j - i < answer:
                break
            start = i
            end = j
            flag = True
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    flag = False
                    break
            if flag:
                if answer < j - i + 1:
                    answer = j - i + 1

    return answer