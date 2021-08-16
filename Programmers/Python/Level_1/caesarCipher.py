def solution(s, n):
    answer = ''
    for i in s:
        if(ord(i) == 32):
            answer += i
        elif(ord(i) >= 97):
            if(ord(i)+n > 122):
                answer += chr(ord(i)+n-26)
            else:
                answer += chr(ord(i)+n)
        else:
            if(ord(i)+n > 90):
                answer += chr(ord(i)+n-26)
            else:
                answer += chr(ord(i)+n)
    return answer
