def solution(n,m):
    answer = 0
    for i in range(n, m + 1):
        reverse = 0
        num = str(i)
        for j in range(len(num) - 1, -1, -1):
            reverse *= 10
            reverse += ord(num[j]) - ord('0')
        if i == reverse:
            answer += 1
 
    return answer