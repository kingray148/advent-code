# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 21:46:07 2021
weblink for the puzzle:
https://adventofcode.com/2021/day/1

@author: TK
"""

def readData(file):
    with open(file, 'r') as f:
        input = ''.join(f.readlines()).split('\n')
        input = [int(x) for x in input]
        #print(input[0])
        return input

def findLNumWindow(data, window_size):
    count = 0
    for i in range(0, len(data)-window_size):
        if data[i+window_size] > data[i]:
            count += 1
    return count

if __name__ == '__main__':
    print(findLNumWindow(readData('..\\files\Sonar Sweep data.txt'),1))
    print(findLNumWindow(readData('..\\files\Sonar Sweep data.txt'),3))