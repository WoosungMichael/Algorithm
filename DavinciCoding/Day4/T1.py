N = int(input())
list1 = list(map(int, input().split()))

M = int(input())
list2 = list(map(int, input().split()))

for i in list2:
    if(i in list1):
        print("yes", end=" ")
    else:
        print("no", end=" ")
