import copy
T = int(input())

for i in range(T):
    str = input()
    cnt = [0] * 26
    for i in str:
        if i != ' ':
            cnt[ord(i)-ord('a')] += 1
    tmp = copy.deepcopy(cnt)
    cnt.sort(reverse=True)
    if cnt[0] == cnt[1]:
        print("?")
    else:
        print(chr(tmp.index(cnt[0]) + ord('a')))
