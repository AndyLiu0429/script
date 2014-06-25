# -*- coding: utf-8 -*-

__author__ = 'liutianyuan'

import os

nums = []
global count
count = 0

def sort(nums):
    if len(nums) == 1:
        return nums
    middle = len(nums) / 2
    left_num = sort(nums[:middle])
    right_num = sort(nums[middle:])
    return merge(left_num, right_num)

def merge(left, right):
    global count
    result = []
    li = 0
    ri = 0
    while(True):
        if left[li] < right[ri]:
            result.append(left[li])
            li += 1
        elif left[li] == right[ri]:
            result.append(left[li])
            result.append(right[ri])
            li += 1
            ri += 1
        elif left[li] > right[ri]:
            result.append(right[ri])
            count += len(left[li:])
            ri += 1
        if not (li < len(left) and ri < len(right)):
            break

    if li < len(left):
        result.extend(left[li:])
    elif ri < len(right):
        result.extend(right[ri:])
    return result

x = []
with open('/Users/liutianyuan/Downloads/IntegerArray .txt','r') as f:
    for line in f.readlines():
        x.append(int(line.split()[0]))

sort_x = sort(x)
print count