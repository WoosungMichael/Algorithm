from itertools import product

# Defining main function


def main():
    # write your codes!
    s = input().replace(';', ' ')
    A = list(map(str, s.split(' ')))
    num = 1
    while(1):
        for i in product(["0", "1"], repeat=num):
            a = 1
            b = 0
            c = 0
            d = 1
            for j in i:
                if j == "0":
                    a += b
                    c += d
                else:
                    b += a
                    d += c
            if(str(a) == A[0] and str(b) == A[1] and str(c) == A[2] and str(d) == A[3]):
                print(" ".join(i))
                exit()
        num += 1


if __name__ == "__main__":
    main()
