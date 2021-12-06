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
#  1. INTEGER_ARRAY stockPrices
#  2. INTEGER k
#

def solution(stockPrices, k):
    # Write your code here
    cnt = 0
    tmp = 0
    tmp_num = stockPrices[0]
    if k == 1:
        return len(stockPrices)
    for i in stockPrices:
        if tmp_num < i:
            tmp += 1
        else:
            if tmp >= k - 1:
                cnt += tmp - k + 2
            tmp = 0
        tmp_num = i
    if tmp >= k - 1:
        cnt += tmp - k + 2
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stockPrices_count = int(input().strip())

    stockPrices = []

    for _ in range(stockPrices_count):
        stockPrices_item = int(input().strip())
        stockPrices.append(stockPrices_item)

    k = int(input().strip())

    result = solution(stockPrices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
