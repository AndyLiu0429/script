#coding = utf-8

import os
global heap
global mapping
global visited
global adj_list
global min_dist

heap = []
mapping = []
visited = []
min_dist = []

def extract_min():
    print heap
    last = len(heap)-1
    swap(0, last)
    swap_map(0, last)
    vertex, dist = mapping.pop(last), heap.pop(last)
    drill_down(0)
    return vertex, dist

def swap(n, m):
    x = heap[n]
    heap[n] = heap[m]
    heap[m] = x

def swap_map(n, m):
    x = mapping[n]
    mapping[n] = mapping[m]
    mapping[m] = x

def insert(vertex, num):
    heap.append(num)
    mapping.append(vertex)
    i =heap.index(num)
    bubble_up(i)

def bubble_up(i):
    while i >=1 and heap[i] < heap[(i-1)/2]:
        swap(i, (i-1)/2)
        swap_map(i, (i-1)/2)
        i = (i-1) / 2

def drill_down(i):
    def min(x,y):
        if y > len(heap)-1 or heap[x] < heap[y]:
            return x
        else:
            return y

    while 2*i+1 < len(heap):
        min_indx = min(2*i+1, 2*i+2)
        if heap[i] > heap[min_indx]:
            swap(i, min_indx)
            swap_map(i, min_indx)
            i = min_indx
        else:
            break

def update(vertex, vertex_dist):
    for (neighbor, dist) in adj_list[vertex-1]:
        if neighbor not in visited:
            if neighbor not in mapping:
                insert(neighbor, dist+vertex_dist)
            else:
                index = mapping.index(neighbor)
                origin_dist = heap[index]
                if dist + vertex_dist < origin_dist:
                    heap[index] = dist + vertex_dist
                    bubble_up(index)



def get_adjacent_list():
    result = []
    with open('/Users/liutianyuan/Downloads/dijkstraData.txt','r') as f:
        for line in f.readlines():
            row = []
            nei = line.split()[1:]
            for r in nei:
                row.append(tuple([int(i) for i in r.split(',')]))
            result.append(row)
    return result

def Dijska():
    global adj_list
    #adj_list = [[(2,1),(3,4)],
                #[(1,2),(3,2)],
                #[(1,4),(2,2)]]
    adj_list = get_adjacent_list()
    total_vertex = len(adj_list)
    for (vertex, dist) in adj_list[0]:
        insert(vertex, dist)
    visited.append(1)
    min_dist.append(0)
    for _ in range(total_vertex-1):
        vertex, dist = extract_min()
        visited.append(vertex)
        min_dist.append(dist)
        update(vertex, dist)

    print visited
    print min_dist
    res = [7,37,59,82,99,115,133,165,188,197]
    print  [min_dist[visited.index(num)] for num in res]

if __name__ == '__main__':
    Dijska()

#2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068
#[(1, 0), (114, 508), (140, 546), (92, 647), (145, 648), (129, 676), (70, 743), (9, 745), (199, 815), (65, 826), (80, 982)]
