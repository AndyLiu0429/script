
def read():
    value_dict = {}
    file_dir = '/Users/liutianyuan/Downloads/knapsack1.txt'
    weight_dict = {}
    index = 1
    with open(file_dir) as f:
        for line in f.readlines():
            temp = line.split()
            value_dict[index] = int(temp[0])
            weight_dict[index] = int(temp[1])
            index += 1
    return value_dict, weight_dict

def main():
    values, weights = read()
    print len(values), len(weights)
    matrix = [[0 for _ in range(10001)] for i in range(101)]
    matrix[0] = [0 for i in range(10001)]
    for index in range(1,101):
        for weight in range(10001):
            last = matrix[index-1][weight]
            if weights[index] > weight:
                matrix[index][weight] = last
            else:
                now = matrix[index-1][weight - weights[index]] + values[index]
                matrix[index][weight] = max(last, now)
    print matrix[100][10000]

if __name__ == '__main__':
    main()