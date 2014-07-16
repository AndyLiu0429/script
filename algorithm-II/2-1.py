
def import_data():
    """
    don't forget minus 1!
    """
    result = []
    with open('/Users/liutianyuan/Downloads/clustering1.txt','r') as f:
        for line in f.readlines():
            raw = [int(i) for i in line.split()]
            result.append([(raw[0]-1, raw[1]-1), raw[2]])
    return result

def find(index, forest):
    while forest[index] != -1:
        index = forest[index]
    return index

def union(id1, id2, forest):
    forest[id1] = id2

def main():
    k = 4
    edges = import_data()
    edges.sort(key = lambda x:x[1])
    clusters = [-1 for i in range(1,501)]
    cluster_num = 500
    #print edges[:10]
    while cluster_num > k:
        now_edge, edge_cost = edges[0]
        #print now_edge, edge_cost
        edges = edges[1:]
        root_1 = find(now_edge[0], clusters)
        root_2 = find(now_edge[1], clusters)
        if root_1 == root_2:
            continue
        else:
            union(root_1, root_2, clusters)
            cluster_num -= 1
    max_pair ,max_cost = edges[0]
    edges = edges[1:]
    while find(max_pair[0],clusters) == find(max_pair[1], clusters):
        max_pair, max_cost = edges[0]
        edges = edges[1:]
    print find(max_pair[0],clusters), find(max_pair[1], clusters)
    print max_pair, max_cost
if __name__ == '__main__':
    #print import_data()
    main()