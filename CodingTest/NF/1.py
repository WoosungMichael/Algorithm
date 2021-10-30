def solution(id_list, k):
    answer = 0
    arr = []
    for i in id_list:
        tmp = i.split()
        for l in set(tmp):
            flag = True
            for j in arr:
                if l == j[0]:
                    if j[1] < int(k):
                        j[1] += 1
                    flag = False
                    break
            if flag:
                arr.append([l, 1])
    for i in arr:
        answer += i[1]
    return answer


def main():
    id_list = ["A B C D", "A D", "A B D", "B D"]
    k = 2
    print(solution(id_list, k))


main()
