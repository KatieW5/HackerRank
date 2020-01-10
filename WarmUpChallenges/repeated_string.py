#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if n <= len(s):
        number = s.count("a", 0, n)
    else:
        sub_number = s.count("a")
        add_on = s.count("a", 0, n % len(s))
        multiples = math.floor(n / len(s))
        number = sub_number * multiples + add_on
    return number


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
