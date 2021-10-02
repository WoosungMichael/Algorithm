# Defining main function
def main():
    A = list(map(int, input().split()))

    N = A[0]
    for i in range(1, N+1):
        flag = 1
        for j in range(i+1, N+1):
            if(A[i] < A[j]):
                flag = 0
                print(j, end=" ")
                break
        if(flag == 1 and i != N):
            print(-1, end=" ")
        elif(flag == 1):
            print(-1, end=" ")

    # write your codes!


if __name__ == "__main__":
    main()
