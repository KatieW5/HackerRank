#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    current = 0
    jumps = 0
    while current + 1 < len(c):
        if (current + 2) < len(c):
            if c[current+2] == 0:
                current = current + 2
                jumps += 1
            else:
                current = current + 1
                jumps += 1
        else:
            current = current + 1
            jumps += 1
    return jumps


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
