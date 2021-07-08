def solution(record):
    answer = []
    action = []
    name = {}
    for i in record:
        tmp = list(i.split())
        action.append([tmp[0], tmp[1]])
        if(tmp[0] != "Leave"):
            name[tmp[1]] = tmp[2]
    for i in action:
        str = ""
        if(i[0] == "Enter"):
            str += name[i[1]]
            str += "님이 들어왔습니다."
            answer.append(str)
        elif(i[0] == "Leave"):
            str += name[i[1]]
            str += "님이 나갔습니다."
            answer.append(str)

    return answer
