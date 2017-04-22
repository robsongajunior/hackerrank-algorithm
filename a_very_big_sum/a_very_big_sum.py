#!/bin/python3
# -*- coding: utf-8 -*-


import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
result = 0


for number in arr:
    result = result + number


result = str(result)

sys.stdout.write(result)



