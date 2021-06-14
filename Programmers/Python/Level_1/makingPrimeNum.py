def solution(nums):
    answer=0
    num=[]
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                flag = True
                for p in range(2,nums[i]+nums[j]+nums[k]):
                    if((nums[i]+nums[j]+nums[k])%p==0):
                        flag = False
                        break
                if(flag):
                    answer += 1
    
    return answer