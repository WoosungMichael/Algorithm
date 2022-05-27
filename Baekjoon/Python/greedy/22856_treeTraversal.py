N = int(input())

parent = [0 for _ in range(N + 1)]
left = [0 for _ in range(N + 1)]
right = [0 for _ in range(N + 1)]

for _ in range(N):
    a, b, c = map(int, input().split())
    if b != -1:
        parent[b] = a
    if c != -1:
        parent[c] = a
    left[a] = b
    right[a] = c

end = 1
while right[end] != -1:
    end = right[end]

cnt = 0
node = 1
while True:
    tmp = node
    if left[node] != -1:
        node = left[node]
    elif right[node] != -1:
        node = right[node]
    elif node == end:
        break
    else:
        if left[parent[node]] == node:
            node = parent[node]
            left[node] = -1
        else:
            node = parent[node]
            right[node] = -1
    cnt += 1

print(cnt)