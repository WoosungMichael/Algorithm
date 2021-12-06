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
#  2. INTEGER m
#

def combination(arr, r):
    answer = []

    if r == 0:
        return [[]]

    for i in range(len(arr)):
        element = arr[i]
        tmp = arr[i + 1:]
        for j in combination(tmp, r - 1):
            answer.append([element] + j)

    return answer


def solution(arr, m):
    # Write your code here
    arr.sort()
    arr_list = list(combination(arr, m))
    max = 0
    for i in arr_list:
        min = 1000000000
        for j in range(len(i)):
            if j + 1 < len(i) and i[j+1] - i[j] < min:
                min = i[j+1] - i[j]
        if max < min:
            max = min
    return max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    m = int(input().strip())

    result = solution(arr, m)

    fptr.write(str(result) + '\n')

    fptr.close()
