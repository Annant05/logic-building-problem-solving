#!/bin/python3

#URL: https://www.hackerrank.com/challenges/diagonal-difference/problem

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)

    forward_diff = 0
    reverse_diff = 0
    
    parent = arr
    # child = []
    for i in range(n):
        child = parent[i]
        forward_diff += child[i]
        reverse_diff += child[(n-1)-i]  
    
    abs_diff = abs(forward_diff - reverse_diff)
    return (abs_diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
