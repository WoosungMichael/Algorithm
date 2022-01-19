def solution(n):
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append((arr[i-1]%1234567 + arr[i-2]%1234567)%1234567)
    return arr[-1]
    
# def solution(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return ((solution(n-1) % 1234567) + (solution(n-2) % 1234567))% 1234567

'''
(a+b) % c = ((a%c) + (b%c)) % c
'''