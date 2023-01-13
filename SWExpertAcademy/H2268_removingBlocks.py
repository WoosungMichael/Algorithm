global time, cnt, r, c, flag, v

d = dict()
v = []

def init(R: int, C: int) -> None:
    global time, cnt, r, c, flag, v
    r = R
    c = C
    for i in range(r):
        v.append([])
    time = 0
    cnt = 0

    return


def dropBlocks(mTimestamp: int, mCol: int, mLen: int) -> int:
    global time, cnt, r, c, flag, v
            
    for i in d:
        tmp = []
        for j in range(len(d[i])):
            if d[i][j] + mTimestamp - time >= r:
                cnt -= 1
                continue
            else:
                d[i][j] += mTimestamp - time
                tmp.append(d[i][j])
        d[i] = tmp

    for i in range(mLen):
        if mCol + i in d:
            d[mCol + i].append(0)
        else:
            d[mCol + i] = [0]

    cnt += mLen

    time = mTimestamp


    #######




    for i in d:
        print(i, d[i])





    # for i in range(c):
    #     tmp = []
    #     for j in range(len(v[i])):
    #         v[i][j] += mTimestamp - time
    #         if v[i][j] >= r:
    #             cnt -= 1
    #         else:
    #             tmp.append(v[i][j])
    #     v2.append(tmp)
    # time = mTimestamp
    # v = copy.deepcopy(v2)

    # for i in range(mLen):
    #     v[mCol + i].append(0)

    return cnt


def removeBlocks(mTimestamp: int) -> int:
    global time, cnt, r, c, flag, v
            
    for i in d:
        for j in range(len(d[i])):
            if d[i][j] + mTimestamp - time >= r:
                cnt -= 1
                continue
            else:
                d[i][j] += mTimestamp - time

    for i in d:
        cnt -= 1
        d[i] = d[i][1:]
    
    time = mTimestamp




    #######




    for i in d:
        print(i, d[i])



    
        
    # v2 = []
    # for i in range(c):
    #     tmp = []
    #     flag = 1
    #     for j in range(len(v[i])):
    #         v[i][j] += mTimestamp - time
    #         if v[i][j] >= r:
    #             cnt -= 1
    #         else:
    #             if flag:
    #                 cnt -= 1
    #                 flag = 0
                
    #             else:
    #                 tmp.append(v[i][j])
    #     v2.append(tmp)

    # v = copy.deepcopy(v2)
    # time = mTimestamp

    return cnt




# import copy
# global time, cnt, r, c, flag, v

# v = []

# def init(R: int, C: int) -> None:
#     global i, j, time, cnt, r, c, flag, v
#     r = R
#     c = C
#     for i in range(c):
#         v.append([])
#     time = 0

#     return


# def dropBlocks(mTimestamp: int, mCol: int, mLen: int) -> int:
#     global i, j, time, cnt, r, c, flag, v
    
#     cnt += mLen
#     v2 = []
#     for i in range(c):
#         tmp = []
#         for j in range(len(v[i])):
#             v[i][j] += mTimestamp - time
#             if v[i][j] >= r:
#                 cnt -= 1
#             else:
#                 tmp.append(v[i][j])
#         v2.append(tmp)
#     time = mTimestamp
#     v = copy.deepcopy(v2)

#     for i in range(mLen):
#         v[mCol + i].append(0)

#     return cnt


# def removeBlocks(mTimestamp: int) -> int:
#     global i, j, time, cnt, r, c, flag, v

#     v2 = []
#     for i in range(c):
#         tmp = []
#         flag = 1
#         for j in range(len(v[i])):
#             v[i][j] += mTimestamp - time
#             if v[i][j] >= r:
#                 cnt -= 1
#             else:
#                 if flag:
#                     cnt -= 1
#                     flag = 0
                
#                 else:
#                     tmp.append(v[i][j])
#         v2.append(tmp)

#     v = copy.deepcopy(v2)
#     time = mTimestamp

#     return cnt


import sys

CMD_INIT = 100
CMD_DROP = 200
CMD_REMOVE = 300


def run():
    query = int(input())
    ok = False
    for i in range(query):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            R = int(next(input_iter))
            C = int(next(input_iter))
            init(R, C)
            ok = True
        elif cmd == CMD_DROP:
            mTimestamp = int(next(input_iter))
            mCol = int(next(input_iter))
            mLen = int(next(input_iter))
            ret = dropBlocks(mTimestamp, mCol, mLen)
            ans = int(next(input_iter))
            if ans != ret:
                ok = False
        elif cmd == CMD_REMOVE:
            mTimestamp = int(next(input_iter))
            ret = removeBlocks(mTimestamp)
            ans = int(next(input_iter))
            if ans != ret:
                ok = False
    return ok


if __name__ == '__main__':
    # sys.stdin = open('sample_input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])

    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)
