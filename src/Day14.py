"""
# -*- coding: utf-8 -*-
@Created on 15:47 2022-01-23

@Describe:

@author: TK
"""
import time


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
    print(polymerDict)
    print(repr(initialState))
    result = initialState.copy()
    for i in range(step):
        temp = ''
        for j in range(result-1):
            temp = ''


if __name__ == '__main__':
    time_start = time.perf_counter()  # 记录程序运行开始时间
    print(polymer('..//files//Day 14 data-test.txt', 10))
    time_end = time.perf_counter()  # 记录程序运行结束时间
    print(time_end - time_start)  # 计算程序运行总时长
