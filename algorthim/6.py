#coding = utf-8
import os

res = {}

with open('/Users/liutianyuan/Downloads/algo1-programming_prob-2sum.txt','r') as f:
    for line in f.readlines():
        res[int(line.strip())] = 0

find_num = [i for i in range(-10001, 10000)]
count = 0

for n in find_num:
    for key in res:
        if key == n-key:
            continue
        elif n-key in res:
            count += 1
            print n
            break