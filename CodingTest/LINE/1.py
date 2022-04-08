def checkBlank(str):
    cnt = 0
    for i in str:
        if i == " ":
            cnt += 1
    return cnt

def checkAlpha(str):
    if len(str) < 1:
        return False
    for i in str:
        if ord(i) < ord('A') or (ord('Z') < ord(i) and ord(i) < ord('a')) or ord('z') < ord(i):
            return False
    return True

def solution(logs):
    answer = 0
    for i in logs:
        if len(i) > 100:
            answer += 1
            continue
        if checkBlank(i) != 11:
            answer += 1
            continue
        word_list = i.split()
        if len(word_list) != 12:
            answer += 1
            continue
        if word_list[0] != "team_name" or word_list[3] != "application_name" or word_list[6] != "error_level" or word_list[9] != "message":
            answer += 1
            continue
        if word_list[1] != ":" or word_list[4] != ":" or word_list[7] != ":" or word_list[10] != ":":
            answer += 1
            continue
        if not checkAlpha(word_list[2]) or not checkAlpha(word_list[5]) or not checkAlpha(word_list[8]) or not checkAlpha(word_list[11]):
            answer += 1
            continue
        
    return answer