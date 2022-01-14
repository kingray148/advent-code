"""
# -*- coding: utf-8 -*-
@Created on 1:41 2022-01-06

@Describe:
https://adventofcode.com/2021/day/5

@author: TK
"""


def overlapDots(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        data = []
        for x in lines:
            line = x.split('->')
            #coordinates = ','.join(line)
            #coordinates = coordinates.split(',')
            coordinates = [int(y.strip()) for y in ','.join(line).split(',')]
            data.append(coordinates)
    dots = {}
    for x in data:
        if x[0] == x[2]:
            if x[1] > x[3]:
                for i in range(x[3], x[1]+1):
                    dots[(x[0],i)] = dots.get((x[0],i),0) + 1
            elif x[1] < x[3]:
                for i in range(x[1], x[3]+1):
                    dots[(x[0],i)] = dots.get((x[0],i),0) + 1
        elif x[1] == x[3]:
            if x[0] > x[2]:
                for i in range(x[2], x[0]+1):
                    dots[(i,x[1])] = dots.get((i,x[1]),0) + 1
            elif x[0] < x[2]:
                for i in range(x[0], x[2]+1):
                    dots[(i,x[1])] = dots.get((i,x[1]),0) + 1
    keys = list(dots.keys())
    for x in keys:
        if dots[x] == 1:
            dots.pop(x)
    #print(dots)
    return len(dots)


def overlapDots2(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    data = []
    for x in lines:
        line = x.split('->')
        #coordinates = ','.join(line)
        #coordinates = coordinates.split(',')
        coordinates = [int(y.strip()) for y in ','.join(line).split(',')]
        data.append(coordinates)
    dots = {}
    for x in data:
        if x[0] == x[2]:
            if x[1] > x[3]:
                for i in range(x[3], x[1]+1):
                    dots[(x[0],i)] = dots.get((x[0],i),0) + 1
            elif x[1] < x[3]:
                for i in range(x[1], x[3]+1):
                    dots[(x[0],i)] = dots.get((x[0],i),0) + 1
        elif x[1] == x[3]:
            if x[0] > x[2]:
                for i in range(x[2], x[0]+1):
                    dots[(i,x[1])] = dots.get((i,x[1]),0) + 1
            elif x[0] < x[2]:
                for i in range(x[0], x[2]+1):
                    dots[(i,x[1])] = dots.get((i,x[1]),0) + 1
        elif abs(x[0]-x[2]) == abs(x[1]-x[3]):
            i = x[0]
            j = x[1]
            while i != x[2] + (x[2] - x[0])/abs(x[2] - x[0]):
                dots[(i,j)] = dots.get((i,j),0) + 1
                i += (x[2] - x[0])/abs(x[2] - x[0])
                j += (x[3] - x[1])/abs(x[3] - x[1])
    keys = list(dots.keys())
    for x in keys:
        if dots[x] == 1:
            dots.pop(x)
    #print(dots)
    return len(dots)


if __name__ == '__main__':
    print(overlapDots('..//files//Day 5 data.txt'))
    print(overlapDots2('..//files//Day 5 data.txt'))
