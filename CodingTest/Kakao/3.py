#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solution' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER x
#

def solution(arr, x):
    # Write your code here
    tmp = []
    cnt = 0
    for i in arr:
        cnt += 1

    arr.sort()
    for i in range(len(arr)):
        while True:
            if arr[i] >= 0 and arr[i] - x < 0:
                tmp.append(arr[i])
                break
            elif arr[i] >= 0 and arr[i] - x >= 0 and arr[i] - x not in tmp:
                arr[i] -= x
            elif arr[i] - x >= 0 and arr[i] - 2 * x < 0:
                if arr[i] - x not in tmp:
                    tmp.append(arr[i]-x)
                else:
                    tmp.append(arr[i])
                break

    tmp.sort()
    index = 0

    temp = -1
    answer = []
    for i in range(len(tmp)):
        if temp == tmp[i]:
            while True:
                if tmp[i] + x not in answer:
                    answer.append(tmp[i] + x)
                    answer.sort()
                    break
                else:
                    tmp[i] += x
        else:
            answer.append(tmp[i])
        temp = tmp[i]

    answer.sort()
    while True:
        if index >= cnt or (index < cnt and index != answer[index]):
            return index
        index += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    x = int(input().strip())

    result = solution(arr, x)

    fptr.write(str(result) + '\n')

    fptr.close()
