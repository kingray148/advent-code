"""
# -*- coding: utf-8 -*-
@Created on 3:51 2022-01-08

@Describe:
https://adventofcode.com/2021/day/8

@author: TK
"""
import time

def calculateDigit(file):
    with open(file, 'r') as f:
        input = f.readlines()
        input = [x.split('|')[1] for x in input]
        input = ' '.join(input).split()
    DigitNum = [2, 3, 4, 7]
    result = 0
    for x in input:
        if len(x) in DigitNum:
            result += 1
    return result

def outputSum(file):
    with open(file, 'r') as f:
        input = f.readlines()
    input = [(''.join(x.split('|'))).split(' ') for x in input]
    #print(input)
    result = []
    for x in input:
        digitMapping = {}
        strMapping = {}
        data = [''.join(sorted(y.strip())) for y in x]
        #datalen = [len(y) for y in data]
        #datalen = sorted(datalen)
        set5 = set()
        set6 = set()
        for y in data:
            if len(y) == 2:
                digitMapping[y] = 1
                strMapping[1] = y
            elif len(y) == 3:
                digitMapping[y] = 7
                #strMapping[7] = y
            elif len(y) == 4:
                digitMapping[y] = 4
                strMapping[4] = y
            elif len(y) == 7:
                digitMapping[y] = 8
                #strMapping[8] = y
            elif len(y) == 5:
                set5.add(y)
            elif len(y) == 6:
                set6.add(y)
        for y in set5:
            if len(set(strMapping[1]).difference(set(y))) == 0:
                digitMapping[y] = 3
                #strMapping[3] = y
            elif len(set(strMapping[4]).difference(set(y))) == 2:
                digitMapping[y] = 2
                #strMapping[2] = y
            else:
                digitMapping[y] = 5
                #strMapping[5] = y
        for y in set6:
            if len(set(strMapping[1]).difference(set(y))) == 1:
                digitMapping[y] = 6
                #strMapping[6] = y
            elif len(set(strMapping[4]).difference(set(y))) == 1:
                digitMapping[y] = 0
                #strMapping[0] = y
            else:
                digitMapping[y] = 9
                #strMapping[9] = y
        result.append(digitMapping[data[-4]]*1000 + digitMapping[data[-3]]*100 + digitMapping[data[-2]]*10 + digitMapping[data[-1]])

    #input = ' '.join(input).split()
    #input = [tuple(sorted(list(x))) for x in input]
    #print(data)
    #print(data[4]==data[-1])
    #print(datalen)
    #print(set5)
    #print(set6)
    #print(digitMapping)
    #print(strMapping)
    return sum(result)


if __name__ == '__main__':
    time_start = time.perf_counter()    #记录程序运行开始时间
    print(calculateDigit('..//files//Day 8 data.txt'))
    print(outputSum('..//files//Day 8 data.txt'))
    time_end = time.perf_counter()      #记录程序运行结束时间
    print(time_end - time_start)