from __future__ import division
import os
filedir = '/Users/liutianyuan/Desktop/iris.txt'

PLANT = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

def import_data():
    """
    import a data
    """
    result = []
    with open(filedir, 'r') as iris_reader:
        for line in iris_reader.readlines():
            tmp = line.strip().split(',')
            res = [float(i) for i in tmp[:4]]
            res.append(tmp[-1])
            result.append(res)
    return result

def split(origin_data, i):
    """
    extract one dimension data
    """
    result = []
    for org in origin_data:
        result.append((org[i], org[4]))
    return result

def chi(ls1, ls2):
    """
    count two lists' chi
    """
    res = 0
    matrix = [ls1]
    matrix.append(ls2)
    N = sum(matrix[0]) + sum(matrix[1])
    for i in range(2):
        for j in range(3):
            E = sum(matrix[i]) * (matrix[0][j]+matrix[1][j]) / N
            if E:
                res += (E - matrix[i][j]) ** 2 / E
    return res

def build(data):
    res = []
    res_mapping = []
    for row in data:
        tmp = [0,0,0]
        tmp[PLANT.index(row[1])] = 1
        res.append(tmp)
        res_mapping.append(row[0])
    return res, res_mapping

def combine(interval,mapping,i):
    for n in range(3):
        interval[i][n] += interval[i+1][n]
    del interval[i+1]
    del mapping[i+1]

def chiMerge(max_interval, i):
    origin_data = import_data()
    my_data = split(origin_data, i)
    my_data.sort(key = lambda x: x[0])
    interval, mapping = build(my_data)
    while len(interval) > max_interval:
        chi_list = []
        for i in range(len(interval)-1):
            chi_list.append(chi(interval[i], interval[i+1]))
        chi_min = min(chi_list)
        combine(interval, mapping, chi_list.index(chi_min))

    print zip(mapping,interval)

if __name__ == '__main__':
    chiMerge(6, 0)











