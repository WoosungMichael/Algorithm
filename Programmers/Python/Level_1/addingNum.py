def solution(absolutes, signs):
    answer = 0
    for index in range(len(absolutes)):
        if(signs[index]==True):
            answer+=absolutes[index]
        else:
            answer-=absolutes[index]
            
    return answer