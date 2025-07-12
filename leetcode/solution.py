#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getPages' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY pages
#  2. INTEGER_ARRAY threshold
#

def getPages(pages, threshold):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pages_count = int(input().strip())

    pages = []

    for _ in range(pages_count):
        pages_item = int(input().strip())
        pages.append(pages_item)

    threshold_count = int(input().strip())

    threshold = []

    for _ in range(threshold_count):
        threshold_item = int(input().strip())
        threshold.append(threshold_item)

    result = getPages(pages, threshold)

    fptr.write(str(result) + '\n')

    fptr.close()
