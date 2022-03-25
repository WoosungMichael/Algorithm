from itertools import permutations 

def isPrime(str):
    if str <= 1:
        return False
    num = int(str)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num_list = []
    for i in numbers:
        num_list.append(i)
    for i in range(len(numbers) - 1):
        num_list.append("")
        
    numbers = list(permutations(num_list, len(numbers)))
    number_list = []
    for i in numbers:
        num = 0
        for j in i:
            if j != "":
                num *= 10
                num += int(j)
        number_list.append(num)
            
    number_list = list(set(number_list))
    for i in number_list:
        if isPrime(i):
            answer += 1
    
    return answer