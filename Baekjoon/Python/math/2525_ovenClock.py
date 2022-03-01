h, m = map(int, input().split())
time = int(input())

print((h + (time + m) // 60) % 24, (time + m) % 60)
