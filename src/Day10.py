"""
# -*- coding: utf-8 -*-
@Created on 0:01 2022-01-09

@Describe:
https://adventofcode.com/2021/day/10

@author: TK
"""


def syntaxErrorScore(file):
    bracketDict = {'>':'<', ')':'(', ']':'[', '}':'{'}
    scoreTable = {')':3, ']':57, '}':1197, '>':25137}
    with open(file, 'r') as f:
        input = f.readlines()
    input = [list(x.strip()) for x in input]
    #print(len(input))
    errorScore = 0
    for x in input:
        stack = []
        for i in range(len(x)):
            if x[i] in bracketDict.values():
                stack.append(x[i])
            elif bracketDict[x[i]] == stack[-1]:
                stack.pop()
            else:
                errorScore += scoreTable[x[i]]
                break
    return errorScore

if __name__ == '__main__':
    print(syntaxErrorScore('..//files//Day 10 data.txt'))
