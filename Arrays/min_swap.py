#!/bin/python3

import math
import os
import random
import re
import sys

def minimumSwaps(arr):
    temp = [0] * (len(arr) + 1)
    # create temp array to hold index of where the element is in array
    # for example, temp[1] = 2 means that arr[2] = 1
    # emp[0] = 0 (it is ignored)
    for pos, val in enumerate(arr):
        temp[val] = pos
        pos += 1
    swaps = 0
    for i in range(len(arr)):
        # if the element is equal to its index plus one
        if arr[i] != i+1:
            swaps += 1
            # set to to the current value
            t = arr[i]
            # set the array at this index to the element to the index plus one
            arr[i] = i+1
            # to swap values, set the original value of the index of the (i+1) value in arr to arr[i]
            arr[temp[i+1]] = t
            # now value t is located as position temp[i+1] and value i+1 is located at position i
            temp[t] = temp[i+1]
            temp[i+1] = i
    return swaps

# This was a selection sort attempt..
# it took too long on the larger inputs
# def minimumSwaps(arr):
#     swap = 0
#     for i in range(len(arr)):
#         min_ind = i
#         min = arr[i]
#         for j in range(i+1,len(arr)):
#             if arr[j] < min:
#                 min_ind = j
#                 min = arr[j]
#         if min != arr[i]:
#             swap += 1
#
#             tmp = arr[i]
#             arr[i] = min
#             arr[min_ind] = tmp
#     return swap

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
