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

def smallCaveTimes(x, pathList):
    lowerCharDict = {}
    for y in pathList:
        if y != 'start' and y != 'end' and y.islower():
            lowerCharDict[y] = lowerCharDict.get(y,0) + 1
    if x == 'start' or x == 'end' or x.isupper() or x not in pathList:
        #print('1')
        #print(x)
        #print(pathList)
        return True
    elif lowerCharDict[x] == 2:
        #print('2')
        return False
    elif lowerCharDict[x] == 1 and max(lowerCharDict.values()) == 2:
        #print(max(lowerCharDict.values()))
        #print('3')
        return False
    else:
        print('4')
        return True

def calPath2(file):
    with open(file, 'r') as f:
        dataInput = f.readlines()
    pathDict = {}
    for x in dataInput:
        a, b = x.split('-')
        a = a.strip()
        b = b.strip()
        pathDict[a] = pathDict.get(a, []) + [b]
        pathDict[b] = pathDict.get(b, []) + [a]
    for x in pathDict.keys():
        while 'start' in pathDict[x]:
            pathDict[x].remove('start')
    del pathDict['end']
    #print(pathDict)
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
            elif smallCaveTimes(x, temp):
                stack.append(temp + [x])
                #print(temp)
                #print(x)
                #a = input("please press some button:")
    #print(pathDict)
    #for x in result:
    #    print(x)
    #print(result)
    return len(result)

if __name__ == '__main__':
    time_start = time.perf_counter()  # 记录程序运行开始时间
    #print(calPath('..//files//Day 12 data.txt'))
    print(calPath2('..//files//Day 12 data.txt'))
    time_end = time.perf_counter()  # 记录程序运行结束时间
    print(time_end - time_start)  # 计算程序运行总时长
