def main():
    num = int(input())
    answer = []
    e = ['-1', '0', '1']
    total, k = 1, 0
    while num > total:
        total += 3 ** (k + 1)
        k += 1

    now = 0
    for i in range(k, -1, -1):
        if i == k:
            answer.append(e[2])
            now += 3 ** i
        elif abs(num - now) < (3 ** i) - (3 ** (i - 1)):
            answer.append(e[1])
        elif num - now < 0:
            answer.append(e[0])
            now -= 3 ** i
        elif num - now > 0:
            answer.append(e[2])
            now += 3 ** i

    answer.reverse()
    print(" ".join(answer))


if __name__ == "__main__":
    main()
