"""
# -*- coding: utf-8 -*-
@Created on 2:33 2022-01-09

@Describe:
https://adventofcode.com/2021/day/11

@author: TK
"""
import numpy as np

def calculateFlash(file, rounds):
    with open(file, 'r') as f:
        input = f.readlines()
    input = ''.join(input).split('\n')
    rows = len(input)
    columns = len(input[0])
    input = [int(x) for x in list(''.join(input))]
    #print(rows)
    #print(columns)
    input = np.reshape(input, (rows, columns))
    input = np.insert(input, 0, -1, axis=0)
    input = np.insert(input, rows+1, -1, axis=0)
    input = np.insert(input, 0, -1, axis=1)
    input = np.insert(input, columns+1, -1, axis=1)
    #print(input)
    flashtimes = 0
    for n in range(0, rounds):
        stack = []
        flashlist = []
        for i in range(1, rows+1):
            for j in range(1, columns+1):
                if input[i,j] < 9:
                    input[i,j] += 1
                elif input[i,j] == 9:
                    input[i,j] = 0
                    flashlist.append([i,j])
                    for a in range(i-1, i+2):
                        for b in range(j-1, j+2):
                            if [a,b] not in flashlist and input[a,b] != -1:
                                stack.append([a,b])
        while stack:
            i, j = stack.pop()
            if [i,j] not in flashlist:
                if input[i, j] < 9:
                    input[i, j] += 1
                elif input[i, j] == 9:
                    input[i, j] = 0
                    flashlist.append([i,j])
                    for a in range(i-1, i+2):
                        for b in range(j-1, j+2):
                            if [a,b] not in flashlist and input[a,b] != -1:
                                stack.append([a,b])
        flashtimes += len(flashlist)
    return flashtimes

def flashSyn(file):
    with open(file, 'r') as f:
        input = f.readlines()
    input = ''.join(input).split('\n')
    rows = len(input)
    columns = len(input[0])
    input = [int(x) for x in list(''.join(input))]
    #print(rows)
    #print(columns)
    input = np.reshape(input, (rows, columns))
    input = np.insert(input, 0, -1, axis=0)
    input = np.insert(input, rows+1, -1, axis=0)
    input = np.insert(input, 0, -1, axis=1)
    input = np.insert(input, columns+1, -1, axis=1)
    #print(input)
    round = 0
    while True:
        round += 1
        stack = []
        flashlist = []
        for i in range(1, rows+1):
            for j in range(1, columns+1):
                if input[i,j] < 9:
                    input[i,j] += 1
                elif input[i,j] == 9:
                    input[i,j] = 0
                    flashlist.append([i,j])
                    for a in range(i-1, i+2):
                        for b in range(j-1, j+2):
                            if [a,b] not in flashlist and input[a,b] != -1:
                                stack.append([a,b])
        while stack:
            i, j = stack.pop()
            if [i,j] not in flashlist:
                if input[i, j] < 9:
                    input[i, j] += 1
                elif input[i, j] == 9:
                    input[i, j] = 0
                    flashlist.append([i,j])
                    for a in range(i-1, i+2):
                        for b in range(j-1, j+2):
                            if [a,b] not in flashlist and input[a,b] != -1:
                                stack.append([a,b])
        if len(flashlist) == rows*columns:
            return round

if __name__ == '__main__':
    print(calculateFlash('..//files//Day 11 data.txt',100))
    print(flashSyn('..//files/Day 11 data.txt'))
