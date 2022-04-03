def solution(name):
    answer = 0
    cnt = 0
    for i in name:
        if i != 'A':
            cnt += 1
            answer += min(ord(i) - ord('A'), ord('Z') + 1 - ord(i))
    
    min_move = 40
    for i in range(len(name)):
        index = 0
        x = 0
        y = 0
        while index < i:
            if name[index] != 'A':
                x = index
            index += 1
        index = 0
        while index + len(name) >= i:
            if name[index] != 'A':
                y = index
            index -= 1
        move_cnt = min(2 * x - y, x - 2 * y)
        if min_move > move_cnt:
            min_move = move_cnt
    
    answer += min_move
    
    return answer