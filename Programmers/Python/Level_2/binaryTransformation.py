def solution(s):
    count = 0
    turn = 0
    
    while(s!="1"):
        turn += 1
        count1 = 0
        for i in s:
            if(i=='0'):
                count1 += 1
        count += count1
        s1=""
        a = (len(s)-count1)
        while(a // 2 > 0):
            if(a%2==0):
                s1+="0"
            else:
                s1+="1"
            a = a // 2
        s1+="1"

        s=s1[::-1]
            
    answer = [turn, count]
    return answer