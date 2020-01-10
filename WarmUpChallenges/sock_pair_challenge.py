import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    total_pairs = 0
    ordered_socks = {}
    for i in ar:
        if i not in ordered_socks.keys():
            ordered_socks[i] = 1
        else:
            ordered_socks[i] += 1
    for i in ordered_socks.keys():
        total_pairs += int(ordered_socks[i] / 2)
    return total_pairs


if __name__ == '__main__':

    print("Enter n")
    n = int(input())
    print("Now enter ar")
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)

