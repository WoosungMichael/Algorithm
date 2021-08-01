import copy


def solution(numbers):
    answer = []
    for i in numbers:
        num = copy.deepcopy(i)
        tmp = format(num, 'b')
        '''
        tmp=""
        while(i>0):
            tmp+=str(i%2)
            i=i//2
        tmp=tmp[::-1]
        '''
        cnt = 3
        while(cnt >= 3):
            num += 1
            cnt = 0
            num2 = copy.deepcopy(num)
            tmp2 = format(num2, 'b')
            '''
            tmp2=""
            while(num2>0):
                tmp2+=str(num2%2)
                num2=num2//2
            tmp2=tmp2[::-1]
            '''
            if(len(tmp) == len(tmp2)):
                for j in range(len(tmp2)):
                    if(tmp[j] != tmp2[j]):
                        cnt += 1
            else:
                for j in range(len(tmp)):
                    if(tmp[-1-j] != tmp2[-1-j]):
                        cnt += 1
                    if(cnt >= 3):
                        break
                for j in range(len(tmp2)-len(tmp)):
                    if(tmp2[j] != 0):
                        cnt += 1
        answer.append(num)

    return answer
