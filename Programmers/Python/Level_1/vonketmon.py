def solution(nums):
    num = len(nums)/2
    list = []
    for i in nums:
        if i not in list:
            list.append(i)
    if(num>len(list)):
        answer=len(list)
    else:
        answer=num
    return answer