def solution(scores):
    answer = ''
    cnt = len(scores)

    for i in range(cnt):
        tmp = []
        sum = 0
        for j in range(cnt):
            sum += scores[j][i]
            tmp.append(scores[j][i])
            if(i == j):
                score = scores[j][i]
        tmp.sort()
        if(tmp[0] == score or tmp[-1] == score):
            if(tmp.count(score) > 1):
                grade = sum/cnt
            else:
                grade = (sum-score)/(cnt-1)
        else:
            grade = sum/cnt

        if(grade >= 90):
            answer += "A"
        elif(grade >= 80):
            answer += "B"
        elif(grade >= 70):
            answer += "C"
        elif(grade >= 50):
            answer += "D"
        else:
            answer += "F"

    return answer
