#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    n = len(q)
    locations = []
    counts = {}
    done = []

    for i in range(n):
        locations.append((i+1, q.index(i+1)+1))

    print(locations)

    for i in locations:
        if (i[0], i[1]) in done or (i[1], i[0]) in done:
            print("oops")
            continue
        tmp =  new_queue[i[0]-1]
        q[i[0]-1] = q[i[1]-1]
        q[i[1]-1] = tmp

        print("new queue index: ", i[0]-1)
        print("new queue value: ", q[i[0]-1])

        print("new_queue: ", new_queue)
        done.append((i[0], i[1]))

    print(new_queue)

    return 0

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
