# encoding = utf-8
import os

filedir = '/Users/liutianyuan/Downloads/jobs.txt'

def read_file(path):
    result = []
    if os.path.isfile(path):
        with open(path) as f:
            for line in f.readlines():
                result.append([int(r) for r in line.split()])
    return result

def completion_time(job_list):
    weighted_time = 0
    time = 0
    for job in job_list:
        time += job[1]
        weighted_time += job[0] * time
    return weighted_time

def cmp_1(x, y):
    if x[1] < y[1]:
        return -1
    elif x[1] > y[1]:
        return 1
    else:
        return x[2] - y[2]

def cmp_2(x, y):
    pass

def greedy(job_list, sort_func):
    cr_list = [(index, job[0]*1.0/job[1], job[0]) for (index, job) in enumerate(job_list)]
    cr_list.sort(cmp=cmp_1, reverse=True)
    new_list = []
    for cr in cr_list:
        new_list.append(job_list[cr[0]])
    print completion_time(new_list)

if __name__ == '__main__':
    #job_list = [[1,3],[2,4],[1,5]]
    job_list = read_file(filedir)
    greedy(job_list,cmp_1)
