def solution(s):
    answer = ''
    a=s.split(' ')
    for i in range(len(a)-1):
        answer += a[i].capitalize()
        answer += " "
    answer+=a[len(a)-1].capitalize()
    return answer