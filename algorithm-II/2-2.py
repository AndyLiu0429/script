import itertools
import math

def import_data():
    """
    don't forget minus 1!
    """
    result = []
    with open('/Users/liutianyuan/Downloads/c1.txt','rb') as f:
        for line in f.readlines():
            raw = ''.join([i for i in line.split()])
            result.append(raw)
    return result

def find(index, forest):
    tmp_list = []
    while forest[index] != -1:
        tmp_list.append(index)
        index = forest[index]
    root = index
    for each in tmp_list:
        forest[each] = root
    return root

def possible_it(x):
    x = str(x)
    raw = []
    result = []
    for i in x:
        raw.append(i)
    #result.append(x)
    index_list = [i for i in range(len(x))]
    #1
    for i in range(len(x)):
        tmp = raw[:]
        tmp[i] = str((int(raw[i]) + 1) % 2)
        result.append(''.join([str(d) for d in tmp]))

    #2
    for index1, index2 in itertools.combinations(index_list, 2):
        tmp = raw[:]
        tmp[index1] = str((int(raw[index1]) + 1) % 2)
        tmp[index2] = str((int(raw[index2]) + 1) % 2)
        result.append(''.join([str(d) for d in tmp]))
    return result

def union(id1, id2, forest):
    pass

def hamming(x, y):
    total = 0
    for i in range(24):
        if x[i] ^ y[i]:
            total += 1
    return total

def my_hash(x):
    return hash(bin(int(x,2)))

def main():
    #bit_num = 24
    #cl_num = 200000
    #dis = 3
    length = math.pow(2, 24)
    hash_map = {}
    vertex_list = import_data()
    #print vertex_list[:10]
    result = []
    count = 0

    for ve in vertex_list:
        hash_map[ve] = -1

    #print len(vertex_list)
    #print len(hash_map)

    for ve in hash_map.keys():
        tmp = possible_it(ve)
        #print len(tmp)
        for each in tmp:
            if each in hash_map:
                root_1 = find(each, hash_map)
                root_2 = find(ve, hash_map)
                if root_1 != root_2:
                    hash_map[root_1] = root_2


    x = 0
    for count in hash_map:
        if hash_map[count] == -1:
            x += 1
    print x


if __name__ == '__main__':
    #print possible_it('1011')
    main()