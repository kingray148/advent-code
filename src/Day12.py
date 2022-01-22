"""
# -*- coding: utf-8 -*-
@Created on 3:42 2022-01-20

@Describe:
https://adventofcode.com/2021/day/12

@author: TK
"""

import time

def calPath(file):
    with open(file, 'r') as f:
        input = f.readlines()
    pathDict = {}
    for x in input:
        a, b = x.split('-')
        a = a.strip()
        b = b.strip()
        pathDict[a] = pathDict.get(a, []) + [b]
        pathDict[b] = pathDict.get(b, []) + [a]
    for x in pathDict.keys():
        while 'start' in pathDict[x]:
            pathDict[x].remove('start')
    del pathDict['end']
    stack = []
    result = []
    for x in pathDict['start']:
        if x == 'end':
            result.append(['start', x])
        else:
            stack.append(['start', x])
    while stack:
        temp = stack.pop()
        for x in pathDict[temp[-1]]:
            if x == 'end':
                result.append(temp + ['end'])
            elif not(x.islower() and x in temp):
                stack.append(temp + [x])
    #print(pathDict)
    #print(len(result))
    return len(result)


if __name__ == '__main__':
    time_start = time.perf_counter()  # 记录程序运行开始时间
    print(calPath('..//files//Day 12 data.txt'))
    time_end = time.perf_counter()  # 记录程序运行结束时间
    print(time_end - time_start)  # 计算程序运行总时长
