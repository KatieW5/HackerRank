#!/bin/python3

import math
import os
import random
import re
import sys

def check_ind(index, a):
    if index >= len(a):
        return index % len(a)
    else:
        return index
# Complete the rotLeft function below.
def rotLeft(a, d):
    max_index = len(a) - 1
    new_arr = []
    for i in range(len(a)):
        new_arr.append(a[check_ind(i+d, a)])
    return new_arr


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
