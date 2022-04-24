import copy

def solution(square, k):
    for num in range(k):
        for i in range(len(square)):
            for j in range(len(square[i]) - 1 , -1, -1):
                square[i].append(square[i][j])
        for i in range(len(square) - 1, -1, -1):
            square.append(copy.deepcopy(square[i]))
    return square