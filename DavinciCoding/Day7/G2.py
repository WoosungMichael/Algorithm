import copy

cnt = 0
num = 1
n = int(input())
while(cnt < n):
    num_t = copy.deepcopy(num)
    while(num_t % 2 == 0):
        num_t = num_t/2
    while(num_t % 3 == 0):
        num_t = num_t/3
    while(num_t % 5 == 0):
        num_t = num_t/5

    if(num_t == 1):
        cnt += 1

    num += 1

print(num-1)
