lines = [map(int, x.split(' ')) for x in open('/Users/liutianyuan/Downloads/knapsack_big.txt', 'r').read().split('\n')[:-1]]

capacity = lines[0][0]
items = lines[1:]

memo = [0 for cap in range(capacity + 1)]

for i, item in enumerate(items):
    print i
    subproblem = []
    for cap in range(capacity + 1):
        subproblem.append(max(memo[cap], memo[cap - item[1]] + item[0] if cap - item[1] >= 0 else 0))
    memo = subproblem

print memo[-1]