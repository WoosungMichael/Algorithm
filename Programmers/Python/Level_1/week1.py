def solution(price, money, count):
    val = price*(count*(count+1)/2)
    if(val-money>0):
        answer=val-money
    else:
        answer=0
    return answer