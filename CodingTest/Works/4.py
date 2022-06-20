def solution(n):
    answer = 0
    arr = [[]for _ in range(n + 1)]
    arr[0] = 0
    arr[1] = 0
    arr[2] = 2
    arr[3] = 6
    index = 4
    arr_index = 4
    for i in range(len(arr)):
        g_min = 1000000000000
        arr[arr_index].append(index * (index - 1))
        arr[arr_index].append(arr[index - 1] * index)
        if index * (index - 1) < g_min:
            g_min = index * (index - 1)
        for j in arr[i]:
            if j * index < g_min:
                g_min = j * index

        if g_min == index * (index - 1):
            index += 1

    return answer