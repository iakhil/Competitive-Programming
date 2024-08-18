# https://www.hackerrank.com/challenges/separate-the-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def is_valid(s, curr):
    
    while s:
        if s.startswith(curr):
            p = len(curr)
            s = s[p:]
            curr = str(int(curr) + 1)

        else:
            return False
    return True

def separateNumbers(s):
    # Write your code here

    n = len(s)

    if n == 1 or s[0] == '0':
        print("NO")
        return

    for i in range(1, n // 2 + 1):

        curr = s[:i]
        
        if is_valid(str(s), curr):
            print("YES", curr)
            return
        
    print("NO")



if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
