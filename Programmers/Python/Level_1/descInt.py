def solution(n):
    tmp=[]
    for i in str(n):
        tmp.append(i)
    tmp.sort(reverse=True)
    answer = 0
    for i in range(len(tmp)):
        answer=answer*10+int(tmp[i])
    
    return answer