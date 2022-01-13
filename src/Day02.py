# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 21:06:07 2021
weblink for the puzzle:
https://adventofcode.com/2021/day/2



all data are stored in txt file: Day 2 data.txt

@author: TK
"""
def readData(file):
    with open(file, 'r') as f:
        data = f.readlines()
    return data

def calPosition(data):
    horizon = 0
    depth = 0
    for x in data:
        #print(x.split())
        direction, step = x.split()
        if direction == 'forward':
            horizon += int(step)
        elif direction == 'up':
            depth -= int(step)
        elif direction == 'down':
            depth += int(step)
    return [horizon, depth]

def posWithAim(data):
    horizon = 0
    depth = 0
    aim = 0
    for x in data:
        direction, step = x.split()
        if direction == 'down':
            aim += int(step)
        elif direction == 'up':
            aim -= int(step)
        elif direction == 'forward':
            horizon += int(step)
            depth += int(step) * aim
    return horizon*depth

if __name__ == '__main__':
    x = calPosition(readData('..\\files\\Day 2 data.txt'))
    #horizon = x[0]
    #depth = x[1]
    print('Horizon is: ' + str(x[0]) + ', Depth is: ' + str(x[1]) + ', Position is: ' + str(x[0] * x[1]))
    print(posWithAim(readData('..\\files\\Day 2 data.txt')))