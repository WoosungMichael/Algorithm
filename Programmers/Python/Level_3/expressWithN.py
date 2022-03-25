def solution(N, number):
    answer = 0
    make = [[] for i in range(8)]
    
    for i in range(8):
        num_str = ""
        for j in range(i + 1):
            num_str += str(N)
        make[i].append(int(num_str))
    
    if number == N:
        return 1

    for i in range(1, 8):
        for j in range(i):
            for num1 in make[j]:
                for num2 in make[i - j - 1]:
                    make[i].append(num1 + num2)
                    make[i].append(num1 - num2)
                    make[i].append(num1 * num2)
                    if num2 != 0:
                        make[i].append(num1 // num2)
        make[i] = list(set(make[i]))
        if number in make[i]:
            return i + 1
    
    return -1