N = int(input())
A = list(map(int, input().split()))
B = []

for i in range(len(A)):
    for k in range(i+1, len(A)):
        if(A[i] < A[k]):
            B.append(k)
            break

print(B)
