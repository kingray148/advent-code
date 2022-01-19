"""
# -*- coding: utf-8 -*-
@Created on 14:44 2022-01-08

@Describe:

@author: TK
"""

import numpy as np

def riskSum(file):
    with open(file, 'r') as f:
        input = f.readlines()
    columns = len(input[0].strip())
    input = ''.join(input).split('\n')
    input = [int(x) for x in list(''.join(input))]
    rows = int(len(input)/columns)
    #print(columns)
    #print(rows)
    input = np.reshape(input, (rows,columns))
    #print(input)
    #print(input.shape)
    riskSum = 0
    maxnum = np.max(input)
    input = np.insert(input, 0, maxnum, axis=0)
    input = np.insert(input, rows+1, maxnum, axis=0)
    input = np.insert(input, 0, maxnum, axis=1)
    input = np.insert(input, columns+1, maxnum, axis=1)
    #print(input)
    #print(input.shape)
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            if input[i,j] < min(input[i-1,j], input[i,j-1], input[i+1,j], input[i,j+1]):
                riskSum += 1 + input[i,j]
    return riskSum

def top3Basin(file):
    with open(file, 'r') as f:
        input = f.readlines()
    columns = len(input[0].strip())
    input = ''.join(input).split('\n')
    input = [int(x) for x in list(''.join(input))]
    rows = int(len(input)/columns)
    #print(columns)
    #print(rows)
    input = np.reshape(input, (rows,columns))
    #print(input)
    #print(input.shape)
    riskSum = 0
    maxnum = np.max(input)
    input = np.insert(input, 0, maxnum, axis=0)
    input = np.insert(input, rows+1, maxnum, axis=0)
    input = np.insert(input, 0, maxnum, axis=1)
    input = np.insert(input, columns+1, maxnum, axis=1)
    #print(input)
    #print(input.shape)
    basinPoints = []
    result = []
    for i in range(1, rows+1):      #先找出全部数组中的地点
        for j in range(1, columns+1):
            if input[i,j] < min(input[i-1,j], input[i,j-1], input[i+1,j], input[i,j+1]):
                basinPoints.append([i,j])
    for x in basinPoints:
        i, j = x
        basinArea = []
        stack = []
        basinArea.append([i,j])
        stack += [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
        while stack:
            a,b = stack.pop()
            if input[a,b] != 9 and [a,b] not in basinArea:
                basinArea.append([a,b])
                stack += [[a-1,b], [a+1,b], [a,b-1], [a,b+1]]
        result.append(len(basinArea))
    result.sort(reverse=True)
    #print(result)
    return(result[0]*result[1]*result[2])

if __name__ == '__main__':
    print(riskSum('..//files//Day 9 data.txt'))
    print(top3Basin('..//files//Day 9 data.txt'))
