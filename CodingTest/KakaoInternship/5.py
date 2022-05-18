def solution(rc, operations):
    r = len(rc)
    c = len(rc[0])
    cmd_list = [[operations[0], 1]]
    cnt = 0
    for i in range(1, len(operations)):
        if operations[i] == cmd_list[-1][0]:
            cmd_list[-1][1] += 1
        else:
            cmd_list.append([operations[i], 1])

    #cmd[1]로 묶어서 효율성 향상 (반복문 말고 한번에)
    for cmd in cmd_list:
        if cmd[0] == "Rotate":
            for i in range(cmd[1] % (2 * (r + c) - 4)):
                i, j = 0, 0
                tmp = rc[0][0]
                while i < r - 1:
                    rc[i][j] = rc[i + 1][j]
                    i += 1
                while j < c - 1:
                    rc[i][j] = rc[i][j + 1]
                    j += 1
                while i > 0:
                    rc[i][j] = rc[i - 1][j]
                    i -= 1
                while j > 1:
                    rc[i][j] = rc[i][j - 1]
                    j -= 1
                rc[i][j] = tmp
            
        else: 
            for i in range(cmd[1] % r):
                tmp = []
                tmp.append(rc[-1])
                for i in range(len(rc) - 1):
                    tmp.append(rc[i])
                rc = tmp

    return rc

# def solution(rc, operations):
#     r = len(rc)
#     c = len(rc[0])
#     cmd_list = [[operations[0], 1]]
#     cnt = 0
#     for i in range(1, len(operations)):
#         if operations[i] == cmd_list[-1][0]:
#             cmd_list[-1][1] += 1
#         else:
#             cmd_list.append([operations[i], 1])

#     for cmd in cmd_list:
#         if cmd[0] == "Rotate":
#             for i in range(cmd[1] % (2 * (r + c) - 4)):
#                 i, j = 0, 0
#                 tmp = rc[0][0]
#                 while i < r - 1:
#                     rc[i][j] = rc[i + 1][j]
#                     i += 1
#                 while j < c - 1:
#                     rc[i][j] = rc[i][j + 1]
#                     j += 1
#                 while i > 0:
#                     rc[i][j] = rc[i - 1][j]
#                     i -= 1
#                 while j > 1:
#                     rc[i][j] = rc[i][j - 1]
#                     j -= 1
#                 rc[i][j] = tmp
            
#         else:
#             for i in range(cmd[1] % r):
#                 tmp = []
#                 tmp.append(rc[-1])
#                 for i in range(len(rc) - 1):
#                     tmp.append(rc[i])
#                 rc = tmp

#     return rc


# -----------------------------------------------------------------------------------------------------------------------


# def solution(rc, operations):
#     r = len(rc)
#     c = len(rc[0])
#     for cmd in operations:
#         if cmd == "Rotate":
#             i, j = 0, 0
#             tmp = rc[0][0]
#             while i < r - 1:
#                 rc[i][j] = rc[i + 1][j]
#                 i += 1
#             while j < c - 1:
#                 rc[i][j] = rc[i][j + 1]
#                 j += 1
#             while i > 0:
#                 rc[i][j] = rc[i - 1][j]
#                 i -= 1
#             while j > 1:
#                 rc[i][j] = rc[i][j - 1]
#                 j -= 1
#             rc[i][j] = tmp
            
#         else:
#             tmp = []
#             tmp.append(rc[-1])
#             for i in range(len(rc) - 1):
#                 tmp.append(rc[i])
#             rc = tmp

#     return rc


