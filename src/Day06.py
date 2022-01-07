"""
# -*- coding: utf-8 -*-
@Created on 2:10 2022-01-07

@Describe:
https://adventofcode.com/2021/day/6

@author: TK
"""


def readData(file):
    with open(file, 'r') as f:
        initialState = f.readlines()
        initialState = [int(x) for x in initialState[0].split(',')]
        return initialState

def lanternFish(initialState, days):
    if days == 0:
        return initialState
    else:
        result = []
        for x in lanternFish(initialState, days-1):
            if x == 0:
                result += [6,8]
            else:
                result += [x-1]
        return result

if __name__ == '__main__':
    print(len(lanternFish(readData('..//files//Day 6 data.txt'), 80)))
