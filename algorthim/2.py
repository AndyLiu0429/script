# -*- coding: utf-8 -*-

__author__ = 'liutianyuan'

import os

global count
count = 0
def sort_each(num):
    global count

    pivot = len(num) -1
    def swap(k, m):
        x = num[k]
        num[k] = num[m]
        num[m] = x
    if len(num) == 1:
        return num
    swap(0, pivot)
    count += len(num) - 1
    i = 1
    for j in range(1, len(num)):
        if num[j] < num[0]:
            swap(j, i)
            i += 1
    swap(0, i-1)
    if i > 1:
        num[:i-1] = sort_each(num[:i-1])
    if i < len(num):
        num[i:] = sort_each(num[i:])
    return num

num = []
with open("/Users/liutianyuan/Downloads/qs.txt",'r') as f:
    for line in f.readlines():
        num.append(int(line.split()[0]))

print sort_each(num)
print count
