def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    for i in range(len(people)):
        if(i >= len(people)):
            break
        if(people[i]+people[-1] <= limit):
            del people[-1]
        answer += 1
    return answer
