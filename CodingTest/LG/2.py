def solution(s, k):
    answer = ''
    word = []
    for i in s:
        word.append(i)
    cnt = 0
    for i in range(len(word) - 1):
        max_alpha = i
        flag = False
        flag1 = False
        for j in range(i + 1, len(word)):
            if ord(word[max_alpha]) > ord(word[j]) and not flag:
                flag1 = True
            if ord(word[max_alpha]) < ord(word[j]):
                max_alpha = j
                flag = True
            elif word[max_alpha] == word[j] and not flag1:
                max_alpha = j
        if flag:
            cnt += 1
            tmp = word[i]
            word[i] = word[max_alpha]
            word[max_alpha] = tmp
        if cnt == k:
            break
    for i in word:
        answer += i
    return answer