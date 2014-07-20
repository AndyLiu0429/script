global count
count = 0
def memoized_fib(num, memo_dict):
    global count
    if num in memo_dict:
        return memo_dict[num]
    else:
        sum1 = memoized_fib(num - 1, memo_dict)
        sum2 = memoized_fib(num - 2, memo_dict)
        memo_dict[num] = sum1 + sum2
        count += 1
        return sum1 + sum2

memoized_fib(num=10, memo_dict={0 : 0, 1 : 1})
print(count)
index1, index2 = 0,0
print index1,index2