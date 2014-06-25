#coding=utf-8

import os
import random

def adjacent_list():
    res= []
    with open('/Users/liutianyuan/Downloads/kargerMinCut.txt') as f:
        for line in f.readlines():
            res.append([int(i) for i in line.split()[1:]])
    return res


def min_cut(adj_list):
    def _merge(vt1, vt2):
        for vi_2 in adj_list[vt2-1]:
            if not vi_2 == vt1:
                adj_list[vt1-1].append(vi_2)
        for i in range(adj_list[vt1-1].count(vt2)):  # eliminate self-loop
            adj_list[vt1-1].remove(vt2)
        adj_list[vt2-1] = []
        for each in adj_list:
            for vi in each:
                if vi == vt2:
                    each[each.index(vi)] = vt1

    vertice = [i+1 for i in range(len(adj_list))]
    while len(vertice) > 2:
        vertex_1 = random.choice(vertice)
        vertex_2 = random.choice(adj_list[vertex_1-1])
        _merge(vertex_1, vertex_2)
        vertice.remove(vertex_2)

    return len(adj_list[vertice[0]-1])

def main():
    adj_list = adjacent_list()
    for i in range(4):
        ad = adj_list[:]
        print len(ad), min_cut(ad)

if __name__ == '__main__':
    main()
