"""
# -*- coding: utf-8 -*-
@Created on 4:33 2022-02-01

@Describe:
https://adventofcode.com/2021/day/15

@author: TK
"""
import time
from heapq import heappop, heappush
import math

def adj(i,j):
    return (i-1,j),(i+1,j),(i,j-1),(i,j+1)

def lowestRiskPath(file):
    with open(file, 'r') as f:
        inputData = f.readlines()
    rows = len(inputData)
    inputData = {(i,j):int(x) for i, row in enumerate(inputData) for j, x in enumerate(row.strip())}
    columns = int(len(inputData)/rows)
    for i in range(rows):
        inputData[(i,columns)] = math.inf
        inputData[(i, -1)] = math.inf
    for j in range(columns):
        inputData[(rows,j)] = math.inf
        inputData[(-1, j)] = math.inf
    adjpool = [(0,(0,0))]
    distDict = {(0,0):0}
    while adjpool:
        dist, vertex = heappop(adjpool)
        #print(vertex)
        if vertex == (rows-1, columns-1):
            return distDict[vertex]
        for v in adj(*vertex):
            if inputData[v] + distDict.get(vertex,math.inf) < distDict.get(v,math.inf):
                #print(v)
                distDict[v] = inputData[v] + distDict.get(vertex,math.inf)
                #print(distDict[v])
                heappush(adjpool,(inputData[v] + distDict.get(vertex,math.inf),v))

def lowestRiskPath2(file):
    with open(file, 'r') as f:
        inputData = f.readlines()
    rows = len(inputData)
    inputData = {(i,j):int(x) for i, row in enumerate(inputData) for j, x in enumerate(row.strip())}
    columns = int(len(inputData)/rows)
    for i in range(rows*5):
        for j in range(columns*5):
            if inputData[(i%rows,j%columns)] + int(i/rows) + int(j/columns) > 9:
                inputData[(i,j)] = (inputData[(i%rows,j%columns)] + int(i/rows) + int(j/columns))%9
            else:
                inputData[(i, j)] = inputData[(i % rows, j % columns)] + int(i / rows) + int(j / columns)
    for i in range(rows*5):
        inputData[(i,columns*5)] = math.inf
        inputData[(i, -1)] = math.inf
    for j in range(columns*5):
        inputData[(rows*5,j)] = math.inf
        inputData[(-1, j)] = math.inf
    adjpool = [(0,(0,0))]
    distDict = {(0,0):0}
    while adjpool:
        dist, vertex = heappop(adjpool)
        #print(vertex)
        if vertex == (rows*5-1, columns*5-1):
            return distDict[vertex]
        for v in adj(*vertex):
            if inputData[v] + distDict.get(vertex,math.inf) < distDict.get(v,math.inf):
                #print(v)
                distDict[v] = inputData[v] + distDict.get(vertex,math.inf)
                #print(distDict[v])
                heappush(adjpool,(inputData[v] + distDict.get(vertex,math.inf),v))


if __name__ == '__main__':
    time_start = time.perf_counter()  # 记录程序运行开始时间
    print(lowestRiskPath('..//files//Day 15 data.txt'))
    print(lowestRiskPath2('..//files//Day 15 data.txt'))
    time_end = time.perf_counter()  # 记录程序运行结束时间
    print(time_end - time_start)  # 计算程序运行总时长
