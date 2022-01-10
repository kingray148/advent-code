# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 21:46:07 2021
weblink for the puzzle:
https://adventofcode.com/2021/day/1

count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?

all data are stored in txt file: sonar sweep data.txt

@author: TK
"""

def readData(file):
    with open(file, 'r') as f:
        input = ''.join(f.readlines()).split('\n')
        input = [int(x) for x in input]
        #print(input[0])
        return input

def findLargerNum(data):
    temp = -1
    count = 0
    for x in data:
        if temp != -1 and x > temp:
            count += 1
        temp = x
    return count

def findLNumWindow(data, window_size):
    count = 0
    for i in range(0, len(data)-window_size):
        if data[i+window_size] > data[i]:
            count += 1
    return count


if __name__ == '__main__':
    print(findLargerNum(readData('..\\files\Sonar Sweep data.txt')))
    print(findLNumWindow(readData('..\\files\Sonar Sweep data.txt'),3))