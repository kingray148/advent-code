"""
# -*- coding: utf-8 -*-
@Created on 15:47 2022-01-23

@Describe:

@author: TK
"""
import time
#import numba
#from helloworld import hello
from collections import Counter

#@numba.jit
def polymer(file, step):
    with open(file, 'r') as f:
        inputData = f.readlines()
    inputData = ''.join(inputData).split('\n')
    polymerDict = {}
    for x in inputData:
        if x != '' and '->' not in x:
            initialState = x.strip()
        elif '->' in x:
            pair, element = x.split('->')
            pair = pair.strip()
            element = element.strip()
            polymerDict[pair] = element
    #print(polymerDict)
    #print(repr(initialState))
    result = initialState
    for i in range(0, step):
        temp = ''
        for j in range(len(result)-1):
            temp += result[j] + polymerDict[result[j:j+2]]
        temp += result[-1]
        result = temp
        print(i)
    resultDict = {}
    for x in list(result):
        resultDict[x] = resultDict.get(x,0) + 1
    print(resultDict)
    return (max(resultDict.values()) - min(resultDict.values()))

def polymer2(file, step):
    with open(file, 'r') as f:
        inputData = f.readlines()
    inputData = ''.join(inputData).split('\n')
    polymerDict = Counter()
    for x in inputData:
        if x != '' and '->' not in x:
            initialString = x.strip()
        elif '->' in x:
            pair, element = x.split('->')
            pair = pair.strip()
            element = element.strip()
            polymerDict[pair] = element
    #print(polymerDict)
    #print(repr(initialState))
    #result = initialState
    initialData = Counter([f"{a}{b}" for a,b in zip(initialString, initialString[1:])])
    #print(initialData)
    for i in range(0, step):
        temp = Counter()
        for s, n in initialData.items():
            #print(s+':'+str(n))
            temp[s[0]+polymerDict[s]] += n
            #print(temp)
            temp[polymerDict[s]+s[1]] += n
            #print(temp)
        initialData = temp
        #print(initialData)
    result = Counter()
    for s, n in initialData.items():
        result[s[0]] += n
        result[s[1]] += n
    for s, n in result.items():
        if n%2 != 1:
            result[s] = int(result[s]/2)
        else:
            result[s] = int((result[s] + 1)/2)
    print(result)
    return result.most_common()[0][1] - result.most_common()[-1][1]

if __name__ == '__main__':
    time_start = time.perf_counter()  # 记录程序运行开始时间
    print(polymer2('..//files//Day 14 data.txt', 40))
    #hello()
    time_end = time.perf_counter()  # 记录程序运行结束时间
    print(time_end - time_start)  # 计算程序运行总时长
