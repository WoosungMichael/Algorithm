M = int(input())
price = list(map(int, input().split()))

j_m, s_m = M, M
j_cnt, s_cnt = 0, 0
for i in range(14):
    if j_m >= price[i]:
        j_cnt += j_m // price[i]
        j_m -= (j_m // price[i]) * price[i]
    if i > 2 and price[i - 3] < price[i -2] and price[i - 2] < price[i - 1] and price[i - 1] < price[i]:
        s_m += s_cnt * price[i]
        s_cnt = 0
    if i > 2 and price[i - 3] > price[i -2] and price[i - 2] > price[i - 1] and price[i - 1] > price[i]:
        if s_m >= price[i]:
            s_cnt += s_m // price[i]
            s_m -= (s_m // price[i]) * price[i]
        
if j_m + j_cnt * price[-1] > s_m + s_cnt * price[-1]:
    print("BNP")
elif j_m + j_cnt * price[-1] < s_m + s_cnt * price[-1]:
    print("TIMING")
else:
    print("SAMESAME")