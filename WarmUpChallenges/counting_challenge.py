import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    num_valleys = 0
    numUp = 0
    numDown = 0

    for i in range(len(s)):
        if s[i] =='U':
            numUp += 1
        else:
            numDown += 1
        if numDown == numUp and s[i] == 'U':
            num_valleys += 1


    return num_valleys


if __name__ == '__main__':

    print("Enter n:")
    n = int(input())

    print("Enter s:")
    s = input()

    result = countingValleys(n, s)
    print(result)