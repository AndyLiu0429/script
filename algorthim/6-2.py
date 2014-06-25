import os
global left_max_heap
global right_min_heap
global medians
global median
left_max_heap = []
right_min_heap = []
medians = []

def swap(x, y, heap):
    n = heap[x]
    heap[x] = heap[y]
    heap[y] = n

def insert_max(n, heap):
    left_max_heap.append(n)
    i = left_max_heap.index(n)
    while i >0 and left_max_heap[i] > left_max_heap[(i-1)/2]:
        swap(i, (i-1)/2, heap)
        i = (i-1)/2

def extract_max(heap):
    def max(x, y):
        if y >= len(heap) or heap[y] < heap[x]:
            return x
        return y

    swap(0, -1, heap)
    max_hit = heap.pop(-1)
    i = 0
    max_index = max(2*i+1, 2*i+2)
    while 2*i+1 < len(heap) and heap[i] < heap[max_index]:
        swap(i, max_index, heap)
        i = max_index
        max_index = max(2*i+1, 2*i+2)
    return max_hit

def insert_min(n, heap):
    right_min_heap.append(n)
    i = right_min_heap.index(n)
    while i >0 and right_min_heap[i] < right_min_heap[(i-1)/2]:
        swap(i, (i-1)/2, heap)
        i = (i-1)/2

def extract_min(heap):
    def min(x, y):
        if y >= len(heap) or heap[y] > heap[x]:
            return x
        return y

    swap(0, -1, heap)
    min_hit = heap.pop(-1)
    i = 0
    min_index = min(2*i+1, 2*i+2)
    while 2*i+1 < len(heap) and heap[i] > heap[min_index]:
        swap(i, min_index, heap)
        i = min_index
        min_index = min(2*i+1, 2*i+2)
    return min_hit

def insert_median(n):
    global median
    if n < median:
        insert_max(n, left_max_heap)
        if len(left_max_heap) > len(right_min_heap):
            left_max = extract_max(left_max_heap)
            insert_min(median, right_min_heap)
            median = left_max

    else:
        insert_min(n, right_min_heap)
        if len(right_min_heap) > len(left_max_heap) + 1:
            right_min = extract_min(right_min_heap)
            insert_max(median, left_max_heap)
            median = right_min


    medians.append(median)

def import_array():
    res = []
    with open('/Users/liutianyuan/Downloads/Median.txt','r') as f:
        for line in f.readlines():
           res.append(int(line.strip()))
    return res

def main():
    global median
    order = import_array()
    #order = [1,5,3,4,6,9,10,8,7,2]
    median = order.pop(0)
    medians.append(median)
    for num in order:
        insert_median(num)
    print medians
    print sum(medians) % 10000

if __name__ == '__main__':
    main()