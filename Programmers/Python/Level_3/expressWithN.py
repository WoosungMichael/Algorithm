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
            for k in range(i - j):
                for jj in make[j]:
                    for kk in make[k]:
                        make[i].append(jj + kk)
                        make[i].append(kk - jj)
                        make[i].append(jj * kk)
                        if kk != 0:
                            make[i].append(jj // kk)
        make[i] = list(set(make[i]))
        if number in make[i]:
            return i + 1
    
    return -1