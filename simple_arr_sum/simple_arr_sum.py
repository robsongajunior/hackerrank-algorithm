#!/bin/python3
# -*- coding: utf-8 -*-


import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
result = 0

for item in arr:
    result = result + item

sys.stdout.write(str(result))

