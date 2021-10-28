def check_square(arr, a, b, n):
    tmp = arr[a][b]
    if tmp == 2:
        return False
    for i in range(a, a+n):
        for j in range(b, b+n):
            if tmp != arr[i][j]:
                return False
    return True


def change_square(arr, a, b, n):
    for i in range(a, a+n):
        for j in range(b, b+n):
            arr[i][j] = 2


def main():
    N = int(input())

    cnt0 = 0
    cnt1 = 0
    arr = []

    for i in range(N):
        arr.append(list(map(int, input().split())))

    i = N
    while i >= 1:
        for j in range(N):
            for k in range(N):
                if j+i <= N and k+i <= N and check_square(arr, j, k, i):
                    if arr[j][k] == 0:
                        cnt0 += 1
                    elif arr[j][k] == 1:
                        cnt1 += 1
                    change_square(arr, j, k, i)
        i //= 2

    print(cnt0)
    print(cnt1)


main()
