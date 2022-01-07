"""
# -*- coding: utf-8 -*-
@Created on 1:56 2022-01-08

@Describe:

@author: TK
"""


def leastFuel(file):
    with open(file, 'r') as f:
        crabposition = f.readlines()
        crabposition = [int(x) for x in crabposition[0].split(',')]
        #print(sum(crabposition))
        #print(len(crabposition))
    positions = set(crabposition)
    fuelQty = []
    for x in positions:
        fuel = 0
        for y in crabposition:
            fuel += abs(x-y)
        fuelQty.append(fuel)
    return min(fuelQty)


if __name__ == '__main__':
    print(leastFuel('..//files//Day 7 data.txt'))
