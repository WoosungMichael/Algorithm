def solution(gems):
    N = len(gems)
    g_dict = {gems[0] : 1, }
    answer = [1, N]
    kind = len(set(gems))
    s, e = 0, 0
    while True:
        if len(g_dict) < kind:
            e += 1
            if e == N:
                break
            if gems[e] in g_dict:
                g_dict[gems[e]] += 1
            else:
                g_dict[gems[e]] = 1
        else:
            if e - s < answer[1] - answer[0]:
                answer = [s + 1, e + 1]
            if g_dict[gems[s]] == 1:
                del g_dict[gems[s]]
            else:
                g_dict[gems[s]] -= 1
            s += 1
            if s == N:
                break
    return answer

# def solution(gems):
#     g_dict = {}
#     cur_index = {}
#     for i in range(len(gems)):
#         if gems[i] in g_dict:
#             g_dict[gems[i]].append(i)
#         else:
#             g_dict[gems[i]] = [i]
#             cur_index[gems[i]] = 0
    
#     length = len(gems)
#     for i in range(length):
#         max_index = 0
#         for j in g_dict:
#             if max_index < g_dict[j][cur_index[j]]:
#                 max_index = g_dict[j][cur_index[j]]
#         if 0 <= max_index - i < length:
#             length = max_index - i
#             answer = [i + 1, max_index + 1]
#             if max_index - i < len(g_dict):
#                 break
#         if cur_index[gems[i]] + 1 >= len(g_dict[gems[i]]):
#             break
#         else:
#             cur_index[gems[i]] += 1
        
    
#     return answer