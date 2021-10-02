# Defining main function
def main():
    A = list(map(str, input().split(';')))
    s = int(A[0])
    v = int(A[1])
    o = int(A[2])
    if(s == 0 or v == 0 or o == 0):
        print("No possible sentence.;")
        exit()
    for i in range(s):
        for j in range(v):
            for k in range(o):
                print(A[3 + i], end=" ")
                print(A[3 + s + j], end=" ")
                print(A[3 + s + v + k], end=";")
    # write your codes!


if __name__ == "__main__":
    main()
