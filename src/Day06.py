"""
# -*- coding: utf-8 -*-
@Created on 2:10 2022-01-07

@Describe:
https://adventofcode.com/2021/day/6

@author: TK
"""

import time

def readData(file):
    with open(file, 'r') as f:
        initialState = f.readlines()
    initialState = [int(x) for x in initialState[0].split(',')]
    data = {}
    for x in initialState:
        data[x] = data.get(x,0) + 1     #使用字典来记录元素个数以在循环次数多的时候压缩计算复杂度和存储空间
    #print(data)
    return data

def lanternFish(data, days):
    for i in range(0, days):
        temp6 = data.get(6,0)
        temp8 = data.get(8,0)
        for x in sorted(data.keys()):
            if x == 0:
                data[6] = data[0]
                data[8] = data[0]
                data[0] = 0
            elif x < 6:
                data[x-1] = data[x]
                data[x] = 0
            elif x == 6:
                data[5] = temp6
            elif x == 7:
                data[6] = data.get(6,0) + data[7]
                data[7] = 0
            elif x == 8:
                data[7] = temp8
    #print(data)
    return data

if __name__ == '__main__':
    time_start = time.perf_counter()    #记录程序运行开始时间
    print(sum(lanternFish(readData('..//files//Day 6 data.txt'), 80).values()))     #day1题目答案计算
    print(sum(lanternFish(readData('..//files//Day 6 data.txt'), 256).values()))    #day2题目答案计算
    time_end = time.perf_counter()      #记录程序运行结束时间
    print(time_end - time_start)        #计算程序运行总时长
