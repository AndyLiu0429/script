#encoding = utf-8
import os
filedir = '/Users/liutianyuan/Downloads/edges.txt'

def import_adj_list(path):
    adj_list = {}
    if os.path.isfile(path):
        with open(path) as f:
            for line in f.readlines():
                edge = [int(i) for i in line.split()]
                adj_list.setdefault(edge[0], [])
                adj_list.setdefault(edge[1], [])
                adj_list[edge[0]].append((edge[1], edge[2]))
                adj_list[edge[1]].append((edge[0], edge[2]))
    return adj_list

def prim_tree(adj_list):
    V = [1]
    S = [i for i in range(2, 501)]
    length = 0
    while S:
        least_cost = find_least(V, S, adj_list)
        length += least_cost[1]
        V.append(least_cost[0])
        S.remove(least_cost[0])
    print length


def find_least(V, S, adj_list):
    cmp_list = []
    for vertex in V:
        for adj in adj_list[vertex]:
            if adj[0] in S:
                cmp_list.append(adj)
    cmp_list.sort(key=lambda x: x[1])
    return cmp_list[0]

def main():
    adj_list = import_adj_list(filedir)
    prim_tree(adj_list)

if __name__ == '__main__':
    main()