def solution(s):
    answer = 0
    x = len(s)
    s = s+s
    for i in range(0, x):
        tmp = s[i:i+x]
        arr = []
        for j in tmp:
            if j == ']' and len(arr) != 0 and arr[-1] == '[':
                del arr[len(arr)-1]
            elif j == '}' and len(arr) != 0 and arr[-1] == '{':
                del arr[len(arr)-1]
            elif j == ')' and len(arr) != 0 and arr[-1] == '(':
                del arr[len(arr)-1]
            else:
                arr.append(j)
        if len(arr) == 0:
            answer += 1

    return answer
