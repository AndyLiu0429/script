#coding = utf-8
__author__ = 'liutianyuan'

import os

stack = []
tmp = []
all = [0 for _ in range(0, 4)]
opt = []
import sys, threading
sys.setrecursionlimit(80000000)
threading.stack_size(67108864)

def dfs(vertice, i):
    global all
    global stack
    all[i-1] = 1
    for adjacent in vertice[i-1]:
        if not all[adjacent-1]:
            dfs(vertice, adjacent)
    stack.append(i)


def reve(vertice):
    num = len(vertice)
    result = [[] for _ in range(num)]
    count = 0
    for vertex in vertice:
        for vi in vertex:
            result[vi-1].append(count+1)
        count += 1
    return result

def dfs_reverse(vertice, i):
    global all
    global res
    all[i-1] = 1
    for adjacent in vertice[i-1]:
        if not all[adjacent-1]:
            dfs_reverse(vertice, adjacent)
    res.append(i)

def import_vertice():
    res = [[] for _ in range(875714)]
    with open('/Users/liutianyuan/Downloads/SCC.txt','r') as f:
        for line in f.readlines():
            res[int(line.split()[0])-1].append(int(line.split()[1]))
    return res

def main():
    vertice = import_vertice()
    #vertice = [[2],[3],[1],[2]]
    global all
    global res
    global tmp, opt
    all = [0 for _ in range(len(vertice))]
    first = vertice[:]
    for r in range(len(all)):
        if not all[r]:
            dfs(first, r+1)
    all = [0 for _ in range(len(stack))]
    tmp = []
    reversed = reve(vertice)
    for v in stack[::-1]:
        if not all[v-1]:
            res = []
            dfs_reverse(reversed, v)
            opt.append(res)
    sort_res = sorted([len(x) for x in opt], reverse = True)
    print sort_res[:5]

if __name__ == '__main__':
    thread=threading.Thread(target=main)
    thread.start()
    #res = import_vertice()
    #print res[875713]