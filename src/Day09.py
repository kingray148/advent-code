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

if __name__ == '__main__':
    print(riskSum('..//files//Day 9 data.txt'))
