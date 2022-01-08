"""
# -*- coding: utf-8 -*-
@Created on 3:51 2022-01-08

@Describe:
https://adventofcode.com/2021/day/8

@author: TK
"""


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

if __name__ == '__main__':
    print(calculateDigit('..//files//Day 8 data.txt'))
