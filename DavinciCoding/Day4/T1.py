N = int(input())
list1 = list(map(int, input().split()))

M = int(input())
list2 = list(map(int, input().split()))

for i in list2:
    if(i in list1):
        print("yes", end=" ")
    else:
        print("no", end=" ")
'''
=> 한쪽을 정렬하여 이에 대한 이진 탐색으로 풀면 시간복잡도 줄일 수 있음
'''
