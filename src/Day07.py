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

def leastFuel2(file):
    with open(file, 'r') as f:
        input = f.readlines()
    input = [int(x) for x in input[0].split(',')]
    position = set(input)
    fuelQtyList = []
    for x in position:
        fuelQty = 0
        for y in input:
            fuelQty += (abs(x - y) + 1)*abs(x - y)/2
        fuelQtyList.append(fuelQty)
    #print(position)
    #print(fuelQtyList)
    return min(fuelQtyList)
    #print(input[0])

if __name__ == '__main__':
    print(leastFuel('..//files//Day 7 data.txt'))
    print(leastFuel2('..//files//Day 7 data.txt'))
